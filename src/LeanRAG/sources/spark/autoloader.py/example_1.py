"""
    The Spark Auto Loader is used to read new data files as they arrive in cloud storage. Further information on Auto Loader is available [here](https://docs.databricks.com/ingestion/auto-loader/index.html)

    Example
    --------
    === "ADLS Gen2"

        ```python
        from rtdip_sdk.pipelines.sources import DataBricksAutoLoaderSource
        from rtdip_sdk.pipelines.utilities import SparkSessionUtility

        # Not required if using Databricks
        spark = SparkSessionUtility(config={}).execute()

        options = {}
        path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}
        format = "{DESIRED-FILE-FORMAT}"

        DataBricksAutoLoaderSource(spark, options, path, format).read_stream()

        OR

        DataBricksAutoLoaderSource(spark, options, path, format).read_batch()
        ```
    === "AWS S3"

        ```python
        from rtdip_sdk.pipelines.sources import DataBricksAutoLoaderSource
        from rtdip_sdk.pipelines.utilities import SparkSessionUtility

        # Not required if using Databricks
        spark = SparkSessionUtility(config={}).execute()

        options = {}
        path = "https://s3.{REGION-CODE}.amazonaws.com/{BUCKET-NAME}/{KEY-NAME}"
        format = "{DESIRED-FILE-FORMAT}"

        DataBricksAutoLoaderSource(spark, options, path, format).read_stream()

        OR

        DataBricksAutoLoaderSource(spark, options, path, format).read_batch()
        ```
    === "GCS"

        ```python
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
        ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        options (dict): Options that can be specified for configuring the Auto Loader. Further information on the options available are [here](https://docs.databricks.com/ingestion/auto-loader/options.html)
        path (str): The cloud storage path
        format (str): Specifies the file format to be read. Supported formats are available [here](https://docs.databricks.com/ingestion/auto-loader/options.html#file-format-options)
    """