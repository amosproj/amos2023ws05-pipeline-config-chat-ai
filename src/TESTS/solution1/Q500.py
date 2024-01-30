#Query 500: I would like to use RTDIP components to read from DataBricksAutoLoaderSource, transform using SEMJsonToPCDMTransformer, then write to SparkEventhubDestination
from rtdip_sdk.pipelines.sources import DataBricksAutoLoaderSource
from rtdip_sdk.pipelines.transformers import SEMJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations import SparkEventhubDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Not required if using Databricks
spark = SparkSessionUtility(config={}).execute()

# Step 1: Read from DataBricksAutoLoaderSource
source_options = {}
source_path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}"
source_format = "{DESIRED-FILE-FORMAT}"

source_df = DataBricksAutoLoaderSource(spark, source_options, source_path, source_format).read_batch()

# Step 2: Transform using SEMJsonToPCDMTransformer
transformer_options = {}
transformer_source_column_name = "body"
transformer_multiple_rows_per_message = True
transformer_status_null_value = "Good"
transformer_change_type_value = "insert"
transformer_timestamp_formats = [
    "yyyy-MM-dd'T'HH:mm:ss.SSSX",
    "yyyy-MM-dd'T'HH:mm:ssX"
]
transformer_filter = None

transformed_df = SEMJsonToPCDMTransformer(
    data=source_df,
    source_column_name=transformer_source_column_name,
    multiple_rows_per_message=transformer_multiple_rows_per_message,
    status_null_value=transformer_status_null_value,
    change_type_value=transformer_change_type_value,
    timestamp_formats=transformer_timestamp_formats,
    filter=transformer_filter
).transform()

# Step 3: Write to SparkEventhubDestination
destination_options = {
    "eventhubs.connectionString": "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}",
    "eventhubs.consumerGroup": "{YOUR-EVENTHUB-CONSUMER-GROUP}",
    "checkpointLocation": "/{CHECKPOINT-LOCATION}/"
}
destination_trigger = "10 seconds"
destination_query_name = "EventhubDestination"
destination_query_wait_interval = None

SparkEventhubDestination(
    spark=spark,
    data=transformed_df,
    options=destination_options,
    trigger=destination_trigger,
    query_name=destination_query_name,
    query_wait_interval=destination_query_wait_interval
).write_stream()