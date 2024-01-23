
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
    