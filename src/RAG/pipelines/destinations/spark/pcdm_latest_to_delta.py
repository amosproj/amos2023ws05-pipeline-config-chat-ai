"""
    The Process Control Data Model Latest Values written to Delta.

    Example
    --------
    ```python
    #PCDM Latest To Delta Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMLatestToDeltaDestination

    pcdm_latest_to_delta_destination = SparkPCDMLatestToDeltaDestination(
        data=df,
        options={
            "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
        },
        destination="{DELTA_TABLE_PATH}",
        mode="append",
        trigger="10 seconds",
        query_name="PCDMLatestToDeltaDestination",
        query_wait_interval=None
    )

    pcdm_latest_to_delta_destination.write_stream()
    ```
    ```python
    #PCDM Latest To Delta Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMLatestToDeltaDestination

    pcdm_latest_to_delta_destination = SparkPCDMLatestToDeltaDestination(
        data=df,
        options={
            "maxRecordsPerFile", "10000"
        },
        destination="{DELTA_TABLE_PATH}",
        mode="overwrite",
        trigger="10 seconds",
        query_name="PCDMLatestToDeltaDestination",
        query_wait_interval=None
    )

    pcdm_latest_to_delta_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be merged into a Delta Table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        destination (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store the latest values
        mode (str): Method of writing to Delta Table - append/overwrite (batch), append/complete (stream)
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Writes Process Control Data Model data to Delta
        """
"""
        Writes streaming Process Control Data Model data to Delta using foreachBatch
        """