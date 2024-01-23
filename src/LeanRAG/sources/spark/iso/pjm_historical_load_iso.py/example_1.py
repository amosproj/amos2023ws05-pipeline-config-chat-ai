"""
    The PJM Historical Load ISO Source is used to read historical load data from PJM API.

    API:               <a href="https://api.pjm.com/api/v1/">https://api.pjm.com/api/v1/</a>  (must be a valid apy key from PJM)

    Historical doc:    <a href="https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition">https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition</a>

    Historical is the same PJM endpoint as Actual, but is called repeatedly within a range established by the start_date & end_date attributes

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import PJMHistoricalLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pjm_source = PJMHistoricalLoadISOSource(
        spark=spark,
        options={
            "api_key": "{api_key}",
            "start_date": "20230510",
            "end_date": "20230520",
        }
    )

    pjm_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        api_key (str): Must be a valid key from PJM, see PJM documentation
        start_date (str): Must be in `YYYY-MM-DD` format.
        end_date (str): Must be in `YYYY-MM-DD` format.

        query_batch_days (int): (optional) Number of days must be < 160 as per PJM & is defaulted to `120`
        sleep_duration (int): (optional) Number of seconds to sleep between request, defaulted to `5` seconds, used to manage requests to PJM endpoint
        request_count (int): (optional) Number of requests made to PJM endpoint before sleep_duration, currently defaulted to `1`

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso"""