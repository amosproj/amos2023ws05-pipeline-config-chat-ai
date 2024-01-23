
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
    