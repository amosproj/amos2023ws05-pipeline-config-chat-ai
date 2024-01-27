"""
    This Spark source class is used to read batch or streaming data from an IoT Hub. IoT Hub configurations need to be specified as options in a dictionary.
    Additionally, there are more optional configurations which can be found [here.](https://github.com/Azure/azure-event-hubs-spark/blob/master/docs/PySpark/structured-streaming-pyspark.md#event-hubs-configuration){ target="_blank" }
    If using startingPosition or endingPosition make sure to check out the **Event Position** section for more details and examples.

    Example
    --------
    ```python
    #IoT Hub Source for Streaming Queries

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

    iot_hub_source = SparkIoThubSource(
        spark=spark,
        options = {
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
            "eventhubs.startingPosition": json.dumps(startingEventPosition),
            "maxEventsPerTrigger" : 1000
        }
    )

    iot_hub_source.read_stream()
    ```
    ```python
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
    ```

    Parameters:
        spark (SparkSession): Spark Session
        options (dict): A dictionary of IoT Hub configurations (See Attributes table below)

    Attributes:
        eventhubs.connectionString (str):  IoT Hub connection string is required to connect to the Eventhubs service. (Streaming and Batch)
        eventhubs.consumerGroup (str): A consumer group is a view of an entire IoT Hub. Consumer groups enable multiple consuming applications to each have a separate view of the event stream, and to read the stream independently at their own pace and with their own offsets. (Streaming and Batch)
        eventhubs.startingPosition (JSON str): The starting position for your Structured Streaming job. If a specific EventPosition is not set for a partition using startingPositions, then we use the EventPosition set in startingPosition. If nothing is set in either option, we will begin consuming from the end of the partition. (Streaming and Batch)
        eventhubs.endingPosition: (JSON str): The ending position of a batch query. This works the same as startingPosition. (Batch)
        maxEventsPerTrigger (long): Rate limit on maximum number of events processed per trigger interval. The specified total number of events will be proportionally split across partitions of different volume. (Stream)

    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Reads batch data from IoT Hubs.
        """
"""
        Reads streaming data from IoT Hubs.
        """