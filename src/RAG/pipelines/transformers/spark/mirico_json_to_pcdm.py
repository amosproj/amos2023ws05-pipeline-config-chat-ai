"""
    Converts a Spark Dataframe column containing a json string created from Mirico to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import MiricoJsonToPCDMTransformer

    mirico_json_to_pcdm_transformer = MiricoJsonToPCDMTransformer(
        data=df
        source_column_name="body",
        status_null_value="Good",
        change_type_value="insert"
        tagname_field="test"
    )

    result = mirico_json_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with SEM data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        status_null_value (optional str): If populated, will replace 'Good' in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
        tagname_field (optional str): If populated, will add the specified field to the TagName column.
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Returns:
            DataFrame: A dataframe with the specified column converted to PCDM
        """