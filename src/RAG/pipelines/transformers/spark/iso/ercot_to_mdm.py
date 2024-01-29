"""
    Converts ERCOT Raw data into Meters Data Model.

    Please check the BaseRawToMDMTransformer for the required arguments and methods.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import ERCOTToMDMTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    ercot_to_mdm_transformer = ERCOTToMDMTransformer(
        spark=spark,
        data=df,
        output_type="usage",
        name=None,
        description=None,
        value_type=None,
        version=None,
        series_id=None,
        series_parent_id=None
    )

    result = ercot_to_mdm_transformer.transform()
    ```
    """