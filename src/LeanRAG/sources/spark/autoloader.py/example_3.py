
        from rtdip_sdk.pipelines.sources import DataBricksAutoLoaderSource
        from rtdip_sdk.pipelines.utilities import SparkSessionUtility

        # Not required if using Databricks
        spark = SparkSessionUtility(config={}).execute()

        options = {}
        path = "gs://{BUCKET-NAME}/{FILE-PATH}"
        format = "{DESIRED-FILE-FORMAT}"

        DataBricksAutoLoaderSource(spark, options, path, format).read_stream()

        OR

        DataBricksAutoLoaderSource(spark, options, path, format).read_batch()
        