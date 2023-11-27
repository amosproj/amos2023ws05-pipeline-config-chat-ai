from dagster import Definitions, ResourceDefinition, graph, op
from databricks.connect import DatabricksSession
from rtdip_sdk.pipelines.sources.spark.delta import SparkDeltaSource
from rtdip_sdk.pipelines.transformers.spark.binary_to_string import BinaryToStringTransformer
from rtdip_sdk.pipelines.transformers.spark.fledge_opcua_json_to_pcdm import FledgeOPCUAJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations.spark.delta import SparkDeltaDestination

# Databricks cluster configuration
databricks_resource = ResourceDefinition.hardcoded_resource(
                    DatabricksSession.builder.remote(
                        host       = "https://{workspace_instance_name}",
                        token      = "{token}",
                        cluster_id = "{cluster_id}"
                        ).getOrCreate()
)

# Pipeline
@op(required_resource_keys={"databricks"})
def pipeline(context):
    spark = context.resources.databricks
    source = SparkDeltaSource(spark, {}, "{path_to_table}").read_batch()
    transformer = BinaryToStringTransformer(source, "{source_column_name}", "{target_column_name}").transform()
    transformer = FledgeOPCUAJsonToPCDMTransformer(transformer, "{source_column_name}").transform()
    SparkDeltaDestination(transformer, {}, "{path_to_table}").write_batch()

@graph
def fledge_pipeline():
    pipeline()

fledge_pipeline_job = fledge_pipeline.to_job(
    resource_defs={ 
                    "databricks": databricks_resource
                   }
)

defs = Definitions(jobs=[fledge_pipeline_job])