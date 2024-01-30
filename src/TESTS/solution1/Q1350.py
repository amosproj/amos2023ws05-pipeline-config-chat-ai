#Query 1350: I would like to use RTDIP components to read from SparkIoThubSource, transform using ECMWFExtractPointToWeatherDataModel, then write to SparkKinesisDestination
from rtdip_sdk.pipelines.sources import SparkIoTHubSource
from rtdip_sdk.pipelines.destinations import SparkKinesisDestination
from rtdip_sdk.pipelines.transformers import ECMWFExtractPointToWeatherDataModel
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Create Spark Session
spark = SparkSessionUtility(config={}).execute()

# Define IoT Hub Source
connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"

startingEventPosition = {
    "offset": -1,
    "seqNo": -1,
    "enqueuedTime": None,
    "isInclusive": True
}

iot_hub_source = SparkIoTHubSource(
    spark=spark,
    options={
        "eventhubs.connectionString": connectionString,
        "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
        "eventhubs.startingPosition": json.dumps(startingEventPosition),
        "maxEventsPerTrigger": 1000
    }
)

# Define ECMWF Extract Point to Weather Data Model Transformer
ecmwf_transformer = ECMWFExtractPointToWeatherDataModel(
    data=iot_hub_source.read_stream()
)

# Define Kinesis Destination
kinesis_destination = SparkKinesisDestination(
    data=ecmwf_transformer.transform(),
    streamName="{KINESIS-STREAM-NAME}",
    region="{AWS-REGION}",
    accessKeyId="{AWS-ACCESS-KEY-ID}",
    secretKey="{AWS-SECRET-ACCESS-KEY}",
    trigger="10 seconds",
    query_name="KinesisDestination",
    query_wait_interval=None
)

# Write to Kinesis Destination
kinesis_destination.write_stream()