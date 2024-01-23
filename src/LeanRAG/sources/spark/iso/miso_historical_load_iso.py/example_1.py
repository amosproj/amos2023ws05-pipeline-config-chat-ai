
    from rtdip_sdk.pipelines.sources import MISOHistoricalLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_source = MISOHistoricalLoadISOSource(
        spark=spark,
        options={
            "start_date": "20230510",
            "end_date": "20230520",
        }
    )

    miso_source.read_batch()
    