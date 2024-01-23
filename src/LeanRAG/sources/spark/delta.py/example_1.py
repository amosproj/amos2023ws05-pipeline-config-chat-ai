"""
    The Spark Delta Source is used to read data from a Delta table.

    Example
    --------
    ```python
    #Delta Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_source = SparkDeltaSource(
        spark=spark,
        options={
            "maxFilesPerTrigger": 1000,
            "ignoreChanges: True,
            "startingVersion": 0
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_source.read_stream()
    ```
    ```python
    #Delta Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_source = SparkDeltaSource(
        spark=spark,
        options={
            "versionAsOf": 0,
            "timestampAsOf": "yyyy-mm-dd hh:mm:ss[.fffffffff]"
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from a Delta table.
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#read-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-source){ target="_blank" }.
        table_name (str): Name of the Hive Metastore or Unity Catalog Delta Table

    Attributes:
        maxFilesPerTrigger (int): How many new files to be considered in every micro-batch. The default is 1000. (Streaming)
        maxBytesPerTrigger (int): How much data gets processed in each micro-batch. (Streaming)
        ignoreDeletes (bool str): Ignore transactions that delete data at partition boundaries. (Streaming)
        ignoreChanges (bool str): Pre-process updates if files had to be rewritten in the source table due to a data changing operation. (Streaming)
        startingVersion (int str): The Delta Lake version to start from. (Streaming)
        startingTimestamp (datetime str): The timestamp to start from. (Streaming)
        withEventTimeOrder (bool str): Whether the initial snapshot should be processed with event time order. (Streaming)
        timestampAsOf (datetime str): Query the Delta Table from a specific point in time. (Batch)
        versionAsOf (int str): Query the Delta Table from a specific version. (Batch)
    """