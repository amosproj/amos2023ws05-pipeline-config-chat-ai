"""
    The Spark Delta Merge Destination is used to merge data into a Delta table. Refer to this [documentation](https://docs.delta.io/latest/delta-update.html#upsert-into-a-table-using-merge&language-python) for more information about Delta Merge.

    Examples
    --------
    ```python
    #Delta Merge Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaMergeDestination

    delta_merge_destination = SparkDeltaMergeDestination(
        data=df,
        destination="DELTA-TABLE-PATH",
        options={
            "checkpointLocation": "/{CHECKPOINT-LOCATION}/"
        },
        merge_condition="`source.id = target.id`"
        when_matched_update_list=None
        when_matched_delete_list=None
        when_not_matched_insert_list=None
        when_not_matched_by_source_update_list=None
        when_not_matched_by_source_delete_list=None
        try_broadcast_join=False
        trigger="10 seconds",
        query_name="DeltaDestination"
        query_wait_interval=None
    )

    delta_merge_destination.write_stream()
    ```
    ```python
    #Delta Merge Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaMergeDestination

    delta_merge_destination = SparkDeltaMergeDestination(
        data=df,
        destination="DELTA-TABLE-PATH",
        options={},
        merge_condition="`source.id = target.id`",
        when_matched_update_list=None,
        when_matched_delete_list=None,
        when_not_matched_insert_list=None,
        when_not_matched_by_source_update_list=None,
        when_not_matched_by_source_delete_list=None,
        try_broadcast_join=False,
        trigger="10 seconds",
        query_name="DeltaDestination"
        query_wait_interval=None
    )

    delta_merge_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be merged into a Delta Table
        destination (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        merge_condition (str): Condition for matching records between dataframe and delta table. Reference Dataframe columns as `source` and Delta Table columns as `target`. For example `source.id = target.id`.
        when_matched_update_list (optional list[DeltaMergeConditionValues]): Conditions(optional) and values to be used when updating rows that match the `merge_condition`. Specify `*` for Values if all columns from Dataframe should be inserted.
        when_matched_delete_list (optional list[DeltaMergeCondition]): Conditions(optional) to be used when deleting rows that match the `merge_condition`.
        when_not_matched_insert_list (optional list[DeltaMergeConditionValues]): Conditions(optional) and values to be used when inserting rows that do not match the `merge_condition`. Specify `*` for Values if all columns from Dataframe should be inserted.
        when_not_matched_by_source_update_list (optional list[DeltaMergeConditionValues]): Conditions(optional) and values to be used when updating rows that do not match the `merge_condition`.
        when_not_matched_by_source_delete_list (optional list[DeltaMergeCondition]): Conditions(optional) to be used when deleting rows that do not match the `merge_condition`.
        try_broadcast_join (optional bool): Attempts to perform a broadcast join in the merge which can leverage data skipping using partition pruning and file pruning automatically. Can fail if dataframe being merged is large and therefore more suitable for streaming merges than batch merges
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (optional str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Merges batch data into a Delta Table.
        """
"""
        Merges streaming data to Delta using foreachBatch
        """