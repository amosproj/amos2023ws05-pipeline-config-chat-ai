"""
    The Spark Delta Sharing Source is used to read data from a Delta table where Delta sharing is configured

    Example
    --------
    ```python
    #Delta Sharing Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSharingSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_sharing_source = SparkDeltaSharingSource(
        spark=spark,
        options={
            "maxFilesPerTrigger": 1000,
            "ignoreChanges: True,
            "startingVersion": 0
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_sharing_source.read_stream()
    ```
    ```python
    #Delta Sharing Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSharingSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_sharing_source = SparkDeltaSharingSource(
        spark=spark,
        options={
            "versionAsOf": 0,
            "timestampAsOf": "yyyy-mm-dd hh:mm:ss[.fffffffff]"
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_sharing_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from a Delta table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available [here](https://docs.databricks.com/data-sharing/read-data-open.html#apache-spark-read-shared-data){ target="_blank" }
        table_path (str): Path to credentials file and Delta table to query

    Attributes:
        ignoreDeletes (bool str): Ignore transactions that delete data at partition boundaries. (Streaming)
        ignoreChanges (bool str): Pre-process updates if files had to be rewritten in the source table due to a data changing operation. (Streaming)
        startingVersion (int str): The Delta Lake version to start from. (Streaming)
        startingTimestamp (datetime str): The timestamp to start from. (Streaming)
        maxFilesPerTrigger (int): How many new files to be considered in every micro-batch. The default is 1000. (Streaming)
        maxBytesPerTrigger (int): How much data gets processed in each micro-batch. (Streaming)
        readChangeFeed (bool str): Stream read the change data feed of the shared table. (Batch & Streaming)
        timestampAsOf (datetime str): Query the Delta Table from a specific point in time. (Batch)
        versionAsOf (int str): Query the Delta Table from a specific version. (Batch)
    """