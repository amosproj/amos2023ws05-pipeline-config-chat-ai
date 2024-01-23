
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
    