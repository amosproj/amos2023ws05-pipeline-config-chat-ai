"""
    The PJM Daily Load ISO Source is used to read daily load data from PJM API. It supports both Actual and Forecast data. Actual will return 1 day, Forecast will return 7 days

    API:           <a href="https://api.pjm.com/api/v1/">https://api.pjm.com/api/v1/</a>  (must be a valid apy key from PJM)

    Actual doc:    <a href="https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition">https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition</a>

    Forecast doc:  <a href="https://dataminer2.pjm.com/feed/load_frcstd_7_day/definition">https://dataminer2.pjm.com/feed/load_frcstd_7_day/definition</a>

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import PJMDailyLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pjm_source = PJMDailyLoadISOSource(
        spark=spark,
        options={
            "api_key": "{api_key}",
            "load_type": "actual"
        }
    )

    pjm_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        api_key (str): Must be a valid key from PJM, see api url
        load_type (str): Must be one of `actual` or `forecast`

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    """
"""
        Gets data from external ISO API.

        Args:
            url_suffix: String to be used as suffix to iso url.

        Returns:
            Raw content of the data received.
        """
"""
        Pulls data from the PJM API and parses the return.

        Returns:
            Raw form of data.
        """
"""
        Creates a new date time column and removes null values. Renames columns

        Args:
            df: Raw form of data received from the API.

        Returns:
            Data after basic transformations.

        """
"""
        Validates the following options:
            - `load_type` must be valid.

        Returns:
            True if all looks good otherwise raises Exception.
        """