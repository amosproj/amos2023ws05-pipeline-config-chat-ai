#Query 1000: I would like to use RTDIP components to read from SparkEventhubSource, transform using BaseRawToMDMTransformer, then write to SparkPCDMToDeltaDestination
from rtdip_sdk.pipelines.sources import SparkEventhubSource
from rtdip_sdk.pipelines.transformers import BaseRawToMDMTransformer
from rtdip_sdk.pipelines.destinations import SparkPCDMToDeltaDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Not required if using Databricks
spark = SparkSessionUtility(config={}).execute()

# Step 1: Read data from SparkEventhubSource
connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"
consumerGroup = "{YOUR-CONSUMER-GROUP}"

eventhub_source = SparkEventhubSource(
    spark=spark,
    options={
        "startingOffsets": "earliest",
        "endingOffsets": "latest",
        "failOnDataLoss": "false"
    },
    connection_string=connectionString,
    consumer_group=consumerGroup
)

data = eventhub_source.read_batch()

# Step 2: Transform the data using BaseRawToMDMTransformer
raw_to_mdm_transformer = BaseRawToMDMTransformer(
    data=data,
    # Specify the required arguments and methods for the transformer
    ...
)

transformed_data = raw_to_mdm_transformer.transform()

# Step 3: Write the transformed data to SparkPCDMToDeltaDestination
pcdm_to_delta_destination = SparkPCDMToDeltaDestination(
    data=transformed_data,
    options={
        "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
    },
    destination_float="{DELTA_TABLE_PATH_FLOAT}",
    destination_string="{DELTA_TABLE_PATH_STRING}",
    destination_integer="{DELTA_TABLE_PATH_INTEGER}",
    mode="append",
    trigger="10 seconds",
    query_name="PCDMToDeltaDestination",
    query_wait_interval=None,
    merge=True,
    try_broadcast_join=False,
    remove_nanoseconds=False,
    remove_duplicates=True
)

pcdm_to_delta_destination.write_batch()