
    from rtdip_sdk.pipelines.sources import PJMHistoricalLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pjm_source = PJMHistoricalLoadISOSource(
        spark=spark,
        options={
            "api_key": "{api_key}",
            "start_date": "20230510",
            "end_date": "20230520",
        }
    )

    pjm_source.read_batch()
    