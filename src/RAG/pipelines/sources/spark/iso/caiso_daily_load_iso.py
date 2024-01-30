"""
    The CAISO Daily Load ISO Source is used to read daily load data from CAISO API.
    It supports multiple types of data. Check the `load_types` attribute.
    <br>API: <a href="http://oasis.caiso.com/oasisapi">http://oasis.caiso.com/oasisapi</a>


    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        load_types (list): Must be a subset of [`Demand Forecast 7-Day Ahead`, `Demand Forecast 2-Day Ahead`, `Demand Forecast Day Ahead`, `RTM 15Min Load Forecast`, `RTM 5Min Load Forecast`, `Total Actual Hourly Integrated Load`]. <br> Default Value - `[Total Actual Hourly Integrated Load]`.
        date (str): Must be in `YYYY-MM-DD` format.

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    """
"""
        Pulls data from the CAISO API and parses the zip files for CSV data.

        Returns:
            Raw form of data.
        """