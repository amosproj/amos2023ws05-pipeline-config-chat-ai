"""
    Converts a Spark DataFrame containing Binary JSON data and related Properties to the Process Control Data Model

    For more information about the SSIP PI Streaming Connector, please see [here.](https://bakerhughesc3.ai/oai-solution/shell-sensor-intelligence-platform/)

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import SSIPPIJsonStreamToPCDMTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    ssip_pi_json_stream_to_pcdm_transformer = SSIPPIJsonStreamToPCDMTransformer(
        spark=spark,
        data=df,
        source_column_name="body",
        properties_column_name="",
        metadata_delta_table=None
    )

    result = ssip_pi_json_stream_to_pcdm_transformer.transform()
    ```

    Parameters:
        spark (SparkSession): Spark Session
        data (DataFrame): DataFrame containing the path and binaryFile data
        source_column_name (str): Spark Dataframe column containing the Binary json data
        properties_column_name (str): Spark Dataframe struct typed column containing an element with the PointType
        metadata_delta_table (optional, str): Name of a metadata table that can be used for PointType mappings
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Returns:
            DataFrame: A dataframe with the provided Binary data converted to PCDM
        """