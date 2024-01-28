"""
    The ERCOT Daily Load ISO Source is used to read daily load data from ERCOT using WebScrapping.
    It supports actual and forecast data.
    <br>API: <a href="https://mis.ercot.com">https://mis.ercot.com</a>


    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        load_type (list): Must be one of `actual` or `forecast`.
        date (str): Must be in `YYYY-MM-DD` format.
        certificate_pfx_key (str): The certificate key data or password received from ERCOT.
        certificate_pfx_key_contents (str): The certificate data received from ERCOT, it could be base64 encoded.

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    """
"""
        Pulls data from the ERCOT API and parses the zip files for CSV data.

        Returns:
            Raw form of data.
        """