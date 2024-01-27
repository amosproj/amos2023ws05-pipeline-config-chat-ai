"""
    Converts a Spark Dataframe column containing a json string created by Fledge to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import FledgeOPCUAJsonToPCDMTransformer

    fledge_opcua_json_to_pcdm_transfromer = FledgeOPCUAJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        status_null_value="Good",
        change_type_value="insert",
        timestamp_formats=[
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ssX",
        ]
    )

    result = fledge_opcua_json_to_pcdm_transfromer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with Json Fledge data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        status_null_value (str): If populated, will replace 'Good' in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
        timestamp_formats (list[str]): Specifies the timestamp formats to be used for converting the timestamp string to a Timestamp Type. For more information on formats, refer to this [documentation.](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Returns:
            DataFrame: A dataframe with the specified column converted to PCDM
        """