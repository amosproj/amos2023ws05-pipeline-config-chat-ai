"""
    The Python Delta Destination is used to write data to a Delta table from a Polars LazyFrame.

     Example
    --------
    === "Azure"

        ```python
        from rtdip_sdk.pipelines.destinations import PythonDeltaDestination

        path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}

        python_delta_destination = PythonDeltaDestination(
            data=LazyFrame
            path=path,
            storage_options={
                "azure_storage_account_name": "{AZURE-STORAGE-ACCOUNT-NAME}",
                "azure_storage_account_key": "{AZURE-STORAGE-ACCOUNT-KEY}"
            },
            mode=:error",
            overwrite_schema=False,
            delta_write_options=None
        )

        python_delta_destination.read_batch()

        ```
    === "AWS"

        ```python
        from rtdip_sdk.pipelines.destinations import PythonDeltaDestination

        path = "https://s3.{REGION-CODE}.amazonaws.com/{BUCKET-NAME}/{KEY-NAME}"

        python_delta_destination = PythonDeltaDestination(
            data=LazyFrame
            path=path,
            options={
                "aws_access_key_id": "{AWS-ACCESS-KEY-ID}",
                "aws_secret_access_key": "{AWS-SECRET-ACCESS-KEY}"
            },
            mode=:error",
            overwrite_schema=False,
            delta_write_options=None
        )

        python_delta_destination.read_batch()
        ```

    Parameters:
        data (LazyFrame): Polars LazyFrame to be written to Delta
        path (str): Path to Delta table to be written to; either local or [remote](https://delta-io.github.io/delta-rs/python/usage.html#loading-a-delta-table){ target="_blank" }. **Locally** if the Table does't exist one will be created, but to write to AWS or Azure, you must have an existing Delta Table
        options (Optional dict): Used if writing to a remote location. For AWS use format {"aws_access_key_id": "<>", "aws_secret_access_key": "<>"}. For Azure use format {"azure_storage_account_name": "storageaccountname", "azure_storage_access_key": "<>"}
        mode (Literal['error', 'append', 'overwrite', 'ignore']): Defaults to error if table exists, 'ignore' won't write anything if table exists
        overwrite_schema (bool): If True will allow for the table schema to be overwritten
        delta_write_options (dict): Options when writing to a Delta table. See [here](https://delta-io.github.io/delta-rs/python/api_reference.html#writing-deltatables){ target="_blank" } for all options
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """
"""
        Writes batch data to Delta without using Spark.
        """
"""
        Raises:
            NotImplementedError: Writing to a Delta table using Python is only possible for batch writes. To perform a streaming read, use the write_stream method of the SparkDeltaDestination component.
        """