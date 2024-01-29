"""
    The MISO Daily Load ISO Source is used to read daily load data from MISO API. It supports both Actual and Forecast data.

    API: <a href="https://docs.misoenergy.org/marketreports/">https://docs.misoenergy.org/marketreports/</a>

    Actual data is available for one day minus from the given date.

    Forecast data is available for next 6 day (inclusive of given date).

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import MISODailyLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_source = MISODailyLoadISOSource(
        spark=spark,
        options={
            "load_type": "actual",
            "date": "20230520",
        }
    )

    miso_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        load_type (str): Must be one of `actual` or `forecast`
        date (str): Must be in `YYYYMMDD` format.

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    """
"""
        Pulls data from the MISO API and parses the Excel file.

        Returns:
            Raw form of data.
        """
"""
        Creates a new `date_time` column and removes null values.

        Args:
            df: Raw form of data received from the API.

        Returns:
            Data after basic transformations.

        """
"""
        Filter outs Actual or Forecast data based on `load_type`.
        Args:
            df: Data received after preparation.

        Returns:
            Final data either containing Actual or Forecast values.

        """
"""
        Validates the following options:
            - `date` must be in the correct format.
            - `load_type` must be valid.

        Returns:
            True if all looks good otherwise raises Exception.

        """