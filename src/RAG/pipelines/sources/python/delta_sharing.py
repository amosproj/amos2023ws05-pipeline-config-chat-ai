"""
    The Python Delta Sharing Source is used to read data from a Delta table with Delta Sharing configured, without using Apache Spark.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.sources import PythonDeltaSharingSource

    python_delta_sharing_source = PythonDeltaSharingSource(
        profile_path="{CREDENTIAL-FILE-LOCATION}",
        share_name="{SHARE-NAME}",
        schema_name="{SCHEMA-NAME}",
        table_name="{TABLE-NAME}"
    )

    python_delta_sharing_source.read_batch()
    ```

    Parameters:
        profile_path (str): Location of the credential file. Can be any URL supported by [FSSPEC](https://filesystem-spec.readthedocs.io/en/latest/index.html){ target="_blank" }
        share_name (str): The value of 'share=' for the table
        schema_name (str): The value of 'schema=' for the table
        table_name (str): The value of 'name=' for the table
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """
"""
        Reads data from a Delta table with Delta Sharing into a Polars LazyFrame.
        """
"""
        Raises:
            NotImplementedError: Reading from a Delta table with Delta Sharing using Python is only possible for batch reads.
        """