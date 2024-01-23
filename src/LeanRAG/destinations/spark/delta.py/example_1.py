"""
    The Spark Delta Destination is used to write data to a Delta table.

    Examples
    --------
    ```python
    #Delta Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaDestination

    delta_destination = SparkDeltaDestination(
        data=df,
        options={
            "checkpointLocation": "/{CHECKPOINT-LOCATION}/"
        },
        destination="DELTA-TABLE-PATH",
        mode="append",
        trigger="10 seconds",
        query_name="DeltaDestination",
        query_wait_interval=None
    )

    delta_destination.write_stream()
    ```
    ```python
    #Delta Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaDestination

    delta_destination = SparkDeltaDestination(
        data=df,
        options={
            "overwriteSchema": True
        },
        destination="DELTA-TABLE-PATH",
        mode="append",
        trigger="10 seconds",
        query_name="DeltaDestination",
        query_wait_interval=None
    )

    delta_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be written to Delta
        options (dict): Options that can be specified for a Delta Table write operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        destination (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table
        mode (optional str): Method of writing to Delta Table - append/overwrite (batch), append/update/complete (stream). Default is append
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (optional str): Unique name for the query in associated SparkSession. (stream) Default is DeltaDestination
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
        txnAppId (str): A unique string that you can pass on each DataFrame write. (Batch & Streaming)
        txnVersion (str): A monotonically increasing number that acts as transaction version. (Batch & Streaming)
        maxRecordsPerFile (int str): Specify the maximum number of records to write to a single file for a Delta Lake table. (Batch)
        replaceWhere (str): Condition(s) for overwriting. (Batch)
        partitionOverwriteMode (str): When set to dynamic, overwrites all existing data in each logical partition for which the write will commit new data. Default is static. (Batch)
        overwriteSchema (bool str): If True, overwrites the schema as well as the table data. (Batch)
    """