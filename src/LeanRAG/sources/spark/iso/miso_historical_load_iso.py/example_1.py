"""
    The MISO Historical Load ISO Source is used to read historical load data from MISO API.

    API: <a href="https://docs.misoenergy.org/marketreports/">https://docs.misoenergy.org/marketreports/</a>

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import MISOHistoricalLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_source = MISOHistoricalLoadISOSource(
        spark=spark,
        options={
            "start_date": "20230510",
            "end_date": "20230520",
        }
    )

    miso_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        start_date (str): Must be in `YYYYMMDD` format.
        end_date (str): Must be in `YYYYMMDD` format.
        fill_missing (str): Set to `"true"` to fill missing Actual load with Forecast load. Default - `true`.

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    """