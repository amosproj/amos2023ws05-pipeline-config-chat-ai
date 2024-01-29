"""
    Converts a Spark DataFrame column containing binaryFile parquet data to the Process Control Data Model.

    This DataFrame should contain a path and the binary data. Typically this can be done using the Autoloader source component and specify "binaryFile" as the format.

    For more information about the SSIP PI Batch Connector, please see [here.](https://bakerhughesc3.ai/oai-solution/shell-sensor-intelligence-platform/)

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import SSIPPIBinaryFileToPCDMTransformer

    ssip_pi_binary_file_to_pcdm_transformer = SSIPPIBinaryFileToPCDMTransformer(
        data=df
    )

    result = ssip_pi_binary_file_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): DataFrame containing the path and binaryFile data
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Returns:
            DataFrame: A dataframe with the provided Binary data convert to PCDM
        """