from rtdip_sdk.pipelines.deploy import DatabricksSDKDeploy, CreateJob, JobCluster, ClusterSpec, Task, NotebookTask, AutoScale, RuntimeEngine, DataSecurityMode, CronSchedule, Continuous, PauseStatus
from rtdip_sdk.authentication.azure import DefaultAuth

def deploy():
    credential = DefaultAuth().authenticate()
    access_token = credential.get_token("2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default").token

    DATABRICKS_WORKSPACE = "{databricks-workspace-url}"

    # Create clusters
    cluster_list = []
    cluster_list.append(JobCluster(
        job_cluster_key="pipeline-cluster",
        new_cluster=ClusterSpec(
            node_type_id="Standard_E4ds_v5",
            autoscale=AutoScale(min_workers=1, max_workers=8),
            spark_version="13.3.x-scala2.12",
            data_security_mode=DataSecurityMode.SINGLE_USER,
            runtime_engine=RuntimeEngine.STANDARD
        )
    ))

    # Create tasks
    task_list = []
    task_list.append(Task(
        task_key="pipeline",
        job_cluster_key="pipeline-cluster",
        notebook_task=NotebookTask(
            notebook_path="{path/to/pipeline.py}"
        )
    ))

    # Create a Databricks Job for the Task
    job = CreateJob(
        name="rtdip-miso-batch-pipeline-job",
        job_clusters=cluster_list,
        tasks=task_list,
        continuous=Continuous(pause_status=PauseStatus.UNPAUSED)
    )

    # Deploy to Databricks
    databricks_pipeline_job = DatabricksSDKDeploy(databricks_job=job, host=DATABRICKS_WORKSPACE, token=access_token, workspace_directory="{path/to/databricks/workspace/directory}")
    databricks_pipeline_job.deploy()

    cluster_list = []
    cluster_list.append(JobCluster(
        job_cluster_key="maintenance-cluster",
        new_cluster=ClusterSpec(
            node_type_id="Standard_E4ds_v5",
            autoscale=AutoScale(min_workers=1, max_workers=3),
            spark_version="13.3.x-scala2.12",
            data_security_mode=DataSecurityMode.SINGLE_USER,
            runtime_engine=RuntimeEngine.PHOTON
        )
    ))

    task_list = []
    task_list.append(Task(
        task_key="rtdip-miso-maintenance-task",
        job_cluster_key="maintenance-cluster",
        notebook_task=NotebookTask(
            notebook_path="{path/to/maintenance.py}"
        )
    ))

    # Create a Databricks Job for the Task
    job = CreateJob(
        name="rtdip-miso-maintenance-job",
        job_clusters=cluster_list,
        tasks=task_list,
        schedule=CronSchedule(
            quartz_cron_expression="4 * * * * ?",
            timezone_id="UTC",
            pause_status=PauseStatus.UNPAUSED
        )
    )

    # Deploy to Databricks
    databricks_pipeline_job = DatabricksSDKDeploy(databricks_job=job, host=DATABRICKS_WORKSPACE, token=access_token, workspace_directory="{path/to/databricks/workspace/directory}")
    databricks_pipeline_job.deploy()

if __name__ == "__main__":
    deploy()