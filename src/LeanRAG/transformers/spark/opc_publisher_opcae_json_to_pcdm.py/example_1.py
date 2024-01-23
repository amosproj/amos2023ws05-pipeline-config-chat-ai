"""
    Converts a Spark Dataframe column containing a json string created by OPC Publisher for A&E(Alarm &Events) data to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import OPCPublisherOPCAEJsonToPCDMTransformer

    opc_publisher_opcae_json_to_pcdm_transformer = OPCPublisherOPCAEJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        timestamp_formats=[
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ssX"
        ],
        filter=None
    )

    result = opc_publisher_opcae_json_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with Json OPC AE data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC AE data
        timestamp_formats (optional list[str]): Specifies the timestamp formats to be used for converting the timestamp string to a Timestamp Type. For more information on formats, refer to this [documentation.](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)
        filter (optional str): Enables providing a filter to the data which can be required in certain scenarios. For example, it would be possible to filter on IoT Hub Device Id and Module by providing a filter in SQL format such as `systemProperties.iothub-connection-device-id = "<Device Id>" AND systemProperties.iothub-connection-module-id = "<Module>"`
    """