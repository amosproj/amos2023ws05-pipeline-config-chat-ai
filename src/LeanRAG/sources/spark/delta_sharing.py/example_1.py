
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
    