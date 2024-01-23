
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
    