"""
    The Python ENTSO-E Source is used to read day-ahead prices from ENTSO-E.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import PythonEntsoeSource

    entsoe_source = PythonEntsoeSource(
        api_key={API_KEY},
        start='20230101',
        end='20231001',
        country_code='NL'
    )

    entsoe_source.read_batch()
    ```

    Args:
        api_key (str): API token for ENTSO-E, to request access see documentation [here](https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_authentication_and_authorisation)
        start (str): Start time in the format YYYYMMDD
        end (str): End time in the format YYYYMMDD
        country_code (str): Country code to query from. A full list of country codes can be found [here](https://github.com/EnergieID/entsoe-py/blob/master/entsoe/mappings.py#L48)
        resolution (optional str): Frequency of values; '60T' for hourly values, '30T' for half-hourly values or '15T' for quarterly values
    """
"""
        Attributes:
            SystemType (Environment): Requires Python
        """
"""
        Reads batch from ENTSO-E API.
        """
"""
        Raises:
            NotImplementedError: ENTSO-E connector does not support the stream operation.
        """