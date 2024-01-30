"""
    Converts MISO Raw data into Meters Data Model.

    Please check the BaseRawToMDMTransformer for the required arguments and methods.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import MISOToMDMTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_to_mdm_transformer = MISOToMDMTransformer(
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

    result = miso_to_mdm_transformer.transform()
    ```

    BaseRawToMDMTransformer:
        ::: src.sdk.python.rtdip_sdk.pipelines.transformers.spark.base_raw_to_mdm
    """