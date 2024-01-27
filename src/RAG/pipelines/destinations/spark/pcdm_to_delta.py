"""
    The Process Control Data Model written to Delta.

    Example
    --------
    ```python
    #PCDM Latest To Delta Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMToDeltaDestination

    pcdm_to_delta_destination = SparkPCDMToDeltaDestination(
        data=df,
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
        remove_duplicates-True
    )

    pcdm_to_delta_destination.write_stream()
    ```
    ```python
    #PCDM Latest To Delta Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMToDeltaDestination

    pcdm_to_delta_destination = SparkPCDMToDeltaDestination(
        data=df,
        options={
            "maxRecordsPerFile", "10000"
        },
        destination_float="{DELTA_TABLE_PATH_FLOAT}",
        destination_string="{DELTA_TABLE_PATH_STRING}",
        destination_integer="{DELTA_TABLE_PATH_INTEGER}",
        mode="overwrite",
        trigger="10 seconds",
        query_name="PCDMToDeltaDestination",
        query_wait_interval=None,
        merge=True,
        try_broadcast_join=False,
        remove_nanoseconds=False,
        remove_duplicates-True
    )

    pcdm_to_delta_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be merged into a Delta Table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        destination_float (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store float values.
        destination_string (Optional str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store string values.
        destination_integer (Optional str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store integer values
        mode (str): Method of writing to Delta Table - append/overwrite (batch), append/complete (stream)
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None
        merge (bool): Use Delta Merge to perform inserts, updates and deletes
        try_broadcast_join (bool): Attempts to perform a broadcast join in the merge which can leverage data skipping using partition pruning and file pruning automatically. Can fail if dataframe being merged is large and therefore more suitable for streaming merges than batch merges
        remove_nanoseconds (bool): Removes nanoseconds from the EventTime column and replaces with zeros
        remove_duplicates (bool: Removes duplicates before writing the data

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