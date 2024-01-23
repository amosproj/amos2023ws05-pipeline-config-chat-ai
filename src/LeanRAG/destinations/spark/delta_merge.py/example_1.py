
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
    