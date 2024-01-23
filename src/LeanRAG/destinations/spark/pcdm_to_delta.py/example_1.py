
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
    