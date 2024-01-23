"""
    The Weather Forecast API V1 Multi Source is used to read 15 days forecast from the Weather API. It allows to
    pull weather data for multiple stations and returns all of them in a single DataFrame.

    URL for one station: <a href="https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json">
    https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json</a>

    It takes a list of Weather Stations. Each station item must contain comma separated Latitude & Longitude.

    Examples
    --------
    `["32.3667,-95.4", "51.52,-0.11"]`

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below).

    Attributes:
        stations (list[str]): List of Weather Stations.
        api_key (str): Weather API key.
        language (str): API response language. Defaults to `en-US`.
        units (str): Unit of measurements. Defaults to `e`.
    """