"""
    The Weather Forecast API V1 Source is used to read 15 days forecast from the Weather API.

    URL: <a href="https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json">
    https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json</a>

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below).

    Attributes:
        lat (str): Latitude of the Weather Station.
        lon (str): Longitude of the Weather Station.
        api_key (str): Weather API key.
        language (str): API response language. Defaults to `en-US`.
        units (str): Unit of measurements. Defaults to `e`.
    """