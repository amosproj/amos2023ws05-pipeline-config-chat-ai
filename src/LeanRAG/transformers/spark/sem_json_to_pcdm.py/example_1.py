"""
    Converts a Spark Dataframe column containing a json string created by SEM to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import SEMJsonToPCDMTransformer

    sem_json_to_pcdm_transformer = SEMJsonToPCDMTransformer(
        data=df
        source_column_name="body",
        version=10,
        status_null_value="Good",
        change_type_value="insert"
    )

    result = sem_json_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with SEM data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        version (int): The version for the OBC field mappings. The latest version is 10.
        status_null_value (optional str): If populated, will replace 'Good' in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
    """