
     #IoT Hub Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkIoThubSource
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

    endingEventPosition = {
        "offset": None,
        "seqNo": -1,
        "enqueuedTime": endTime,
        "isInclusive": True
    }

    iot_hub_source = SparkIoThubSource(
        spark,
        options = {
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
            "eventhubs.startingPosition": json.dumps(startingEventPosition),
            "eventhubs.endingPosition": json.dumps(endingEventPosition)
        }
    )

    iot_hub_source.read_batch()
    