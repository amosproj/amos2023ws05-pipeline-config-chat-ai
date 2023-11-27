import json
from datetime import datetime as dt
from dagster import Definitions, graph, op
from dagster_pyspark.resources import pyspark_resource
from rtdip_sdk.pipelines.sources.spark.eventhub import SparkEventhubSource
from rtdip_sdk.pipelines.transformers.spark.binary_to_string import BinaryToStringTransformer
from rtdip_sdk.pipelines.transformers.spark.fledge_opcua_json_to_pcdm import FledgeOPCUAJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations.spark.delta import SparkDeltaDestination

# PySpark cluster configuration
packages = "com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.22,io.delta:delta-core_2.12:2.4.0"
my_pyspark_resource = pyspark_resource.configured(
    {"spark_conf": {"spark.default.parallelism": 1,
                    "spark.jars.packages": packages,
                    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension", 
                    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog"
                    }
    }
)

# EventHub configuration
eventhub_connection_string = "{eventhub_connection_string}"
eventhub_consumer_group = "{eventhub_consumer_group}"

startOffset = "-1"
endTime = dt.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

startingEventPosition = {
  "offset": startOffset,  
  "seqNo": -1,            
  "enqueuedTime": None,   
  "isInclusive": True
}

endingEventPosition = {
  "offset": None,           
  "seqNo": -1,              
  "enqueuedTime": endTime,
  "isInclusive": True
}

ehConf = {
'eventhubs.connectionString' : eventhub_connection_string,
'eventhubs.consumerGroup': eventhub_consumer_group,
'eventhubs.startingPosition' : json.dumps(startingEventPosition),
'eventhubs.endingPosition' : json.dumps(endingEventPosition),
'maxEventsPerTrigger': 1000
}

# Pipeline
@op(required_resource_keys={"spark"})
def pipeline(context):
    spark = context.resources.pyspark.spark_session
    source = SparkEventhubSource(spark, ehConf).read_batch()
    transformer = BinaryToStringTransformer(source, "{source_column_name}", "{target_column_name}").transform()
    transformer = FledgeOPCUAJsonToPCDMTransformer(transformer, "{source_column_name}").transform()
    SparkDeltaDestination(transformer, {}, "{path_to_table}").write_batch()

@graph
def fledge_pipeline():
    pipeline()

fledge_pipeline_job = fledge_pipeline.to_job(
    resource_defs={
                   "spark": my_pyspark_resource
                   }
)

defs = Definitions(jobs=[fledge_pipeline_job])