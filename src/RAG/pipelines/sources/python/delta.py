"""
    The Python Delta Source is used to read data from a Delta table without using Apache Spark, returning a Polars LazyFrame.

     Example
    --------
    === "Azure"

        ```python
        from rtdip_sdk.pipelines.sources import PythonDeltaSource

        path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}

        python_delta_source = PythonDeltaSource(
            path=path,
            version=None,
            storage_options={
                "azure_storage_account_name": "{AZURE-STORAGE-ACCOUNT-NAME}",
                "azure_storage_account_key": "{AZURE-STORAGE-ACCOUNT-KEY}"
            },
            pyarrow_options=None,
            without_files=False
        )

        python_delta_source.read_batch()
        ```
    === "AWS"

        ```python
        from rtdip_sdk.pipelines.sources import PythonDeltaSource

        path = "https://s3.{REGION-CODE}.amazonaws.com/{BUCKET-NAME}/{KEY-NAME}"

        python_delta_source = PythonDeltaSource(
            path=path,
            version=None,
            storage_options={
                "aws_access_key_id": "{AWS-ACCESS-KEY-ID}",
                "aws_secret_access_key": "{AWS-SECRET-ACCESS-KEY}"
            },
            pyarrow_options=None,
            without_files=False
        )

        python_delta_source.read_batch()
        ```

    Parameters:
        path (str): Path to the Delta table. Can be local or in S3/Azure storage
        version (optional int): Specify the Delta table version to read from. Defaults to the latest version
        storage_options (optional dict): Used to read from AWS/Azure storage. For AWS use format {"aws_access_key_id": "<>", "aws_secret_access_key":"<>"}. For Azure use format {"azure_storage_account_name": "<>", "azure_storage_account_key": "<>"}.
        pyarrow_options (optional dict): Data Access and Efficiency options when reading from Delta. See [to_pyarrow_dataset](https://delta-io.github.io/delta-rs/python/api_reference.html#deltalake.table.DeltaTable.to_pyarrow_dataset){ target="_blank" }.
        without_files (optional bool): If True loads the table without tracking files
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """
"""
        Reads data from a Delta table into a Polars LazyFrame
        """
"""
        Raises:
            NotImplementedError: Reading from a Delta table using Python is only possible for batch reads. To perform a streaming read, use the read_stream method of the SparkDeltaSource component.
        """