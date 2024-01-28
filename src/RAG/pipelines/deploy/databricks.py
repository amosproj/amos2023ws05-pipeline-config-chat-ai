"""
    Deploys an RTDIP Pipeline to Databricks Workflows leveraging the Databricks [SDK.](https://docs.databricks.com/dev-tools/sdk-python.html)

    Deploying an RTDIP Pipeline to Databricks requires only a few additional pieces of information to ensure the RTDIP Pipeline Job can be run in Databricks. This information includes:

    - **Cluster**: This can be defined a the Job or Task level and includes the size of the cluster to be used for the job
    - **Task**: The cluster to be used to execute the task, as well as any task scheduling information, if required.

    All options available in the [Databricks Jobs REST API v2.1](https://docs.databricks.com/dev-tools/api/latest/jobs.html) can be configured in the Databricks classes that have been defined in `rtdip_sdk.pipelines.deploy.models.databricks`, enabling full control of the configuration of the Databricks Workflow :

    - `CreateJob`
    - `Task`

    RTDIP Pipeline Components provide Databricks with all the required Python packages and JARs to execute each component and these will be setup on the Workflow automatically during the Databricks Workflow creation.

    Example:
        This example assumes that a PipelineJob has already been defined by a variable called `pipeline_job`

        ```python
        from rtdip_sdk.pipelines.deploy import DatabricksSDKDeploy, CreateJob, JobCluster, ClusterSpec, Task, NotebookTask, ComputeSpecKind, AutoScale, RuntimeEngine, DataSecurityMode

        cluster_list = []
        cluster_list.append(JobCluster(
            job_cluster_key="test_cluster",
            new_cluster=ClusterSpec(
                node_type_id="Standard_E4ds_v5",
                autoscale=AutoScale(min_workers=1, max_workers=3),
                spark_version="13.2.x-scala2.12",
                data_security_mode=DataSecurityMode.SINGLE_USER,
                runtime_engine=RuntimeEngine.PHOTON
            )
        ))

        task_list = []
        task_list.append(Task(
            task_key="test_task",
            job_cluster_key="test_cluster",
            notebook_task=NotebookTask(
                notebook_path="/path/to/pipeline/rtdip_pipeline.py"
            )
        ))

        job = CreateJob(
            name="test_job_rtdip",
            job_clusters=cluster_list,
            tasks=task_list
        )

        databricks_job = DatabricksSDKDeploy(databricks_job=job, host="https://test.databricks.net", token="test_token")

        # Execute the deploy method to create a Workflow in the specified Databricks Environment
        deploy_result = databricks_job.deploy()

        # If the job should be executed immediately, execute the `launch` method
        launch_result = databricks_job.launch()
        ```

    Parameters:
        databricks_job (DatabricksJob): Contains Databricks specific information required for deploying the RTDIP Pipeline Job to Databricks, such as cluster and workflow scheduling information. This can be any field in the [Databricks Jobs REST API v2.1](https://docs.databricks.com/dev-tools/api/latest/jobs.html)
        host (str): Databricks URL
        token (str): Token for authenticating with Databricks such as a Databricks PAT Token or Azure AD Token
        workspace_directory (str, optional): Determines the folder location in the Databricks Workspace. Defaults to /rtdip
    """
"""
        Deploys an RTDIP Pipeline Job to Databricks Workflows. The deployment is managed by the Job Name and therefore will overwrite any existing workflow in Databricks with the same name.
        """
"""
        Launches an RTDIP Pipeline Job in Databricks Workflows. This will perform the equivalent of a `Run Now` in Databricks Workflows
        """