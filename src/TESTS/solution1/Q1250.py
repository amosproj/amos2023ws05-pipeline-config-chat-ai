#Query 1250: I would like to use RTDIP components to read from SparkIoThubSource, transform using OPCPublisherOPCUAJsonToPCDMTransformer, then write to SparkKafkaEventhubDestination

from rtdip_sdk.pipelines.sources import SparkIoTHubSource
from rtdip_sdk.pipelines.transformers import OPCPublisherOPCUAJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations import SparkKafkaEventhubDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Not required if using Databricks
spark = SparkSessionUtility(config={}).execute()

# SparkIoTHubSource
iothub_source = SparkIoTHubSource(
    spark=spark,
    options={
        "eventhubs.connectionString": "{EVENTHUB_CONNECTION_STRING}",
        "eventhubs.consumergroup": "{EVENTHUB_CONSUMER_GROUP}"
    }
)

# OPCPublisherOPCUAJsonToPCDMTransformer
opcpublisher_transformer = OPCPublisherOPCUAJsonToPCDMTransformer(
    data=iothub_source.read_stream(),
    source_column_name="body",
    multiple_rows_per_message=True,
    status_null_value="Good",
    change_type_value="insert",
    timestamp_formats=[
        "yyyy-MM-dd'T'HH:mm:ss.SSSX",
        "yyyy-MM-dd'T'HH:mm:ssX"
    ],
    filter=None
)

# SparkKafkaEventhubDestination
kafka_eventhub_destination = SparkKafkaEventhubDestination(
    spark=spark,
    data=opcpublisher_transformer.transform(),
    options={
        "eventhubs.connectionString": "{EVENTHUB_CONNECTION_STRING}",
        "eventhubs.producerPoolSize": "10"
    },
    trigger="10 seconds",
    query_name="KafkaEventhubDestination",
    query_wait_interval=None
)

kafka_eventhub_destination.write_stream()