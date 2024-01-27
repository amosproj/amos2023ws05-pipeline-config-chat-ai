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
"""
        Pulls data from the MISO API and parses the Excel file.

        Returns:
            Raw form of data.
        """
"""
        Creates a new `Datetime` column, removes null values and pivots the data.

        Args:
            df: Raw form of data received from the API.

        Returns:
            Data after basic transformations and pivoting.

        """
"""
        Filter outs data outside the requested date range.

        Args:
            df: Data received after preparation.

        Returns:
            Final data after all the transformations.

        """
"""
        Validates the following options:
            - `start_date` & `end_data` must be in the correct format.
            - `start_date` must be behind `end_data`.
            - `start_date` must not be in the future (UTC).

        Returns:
            True if all looks good otherwise raises Exception.

        """