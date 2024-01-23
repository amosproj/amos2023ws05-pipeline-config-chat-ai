
    #Eventhub Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkEventhubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility
    import json

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"

    startingEventPosition = {
    "offset": -1,
    "seqNo": -1,
    "enqueuedTime": None,
    "isInclusive": True
    }

    eventhub_source = SparkEventhubSource(
        spark=spark,
        options = {
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
            "eventhubs.startingPosition": json.dumps(startingEventPosition),
            "maxEventsPerTrigger" : 1000
        }
    )

    eventhub_source.read_stream()
    