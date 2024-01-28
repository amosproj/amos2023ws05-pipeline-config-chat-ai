"""
    Base class for all the Weather related sources. Provides common functionality.

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of Weather Source specific configurations.

    """
"""
        Gets data from external Weather Forecast API.

        Args:
            url_suffix: String to be used as suffix to weather url.

        Returns:
            Raw content of the data received.

        """