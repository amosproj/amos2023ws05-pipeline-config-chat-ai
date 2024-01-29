"""
    The Python MFFBAS Source is used to read the Standaard Jaar Verbruiksprofielen (Standard Consumption Profiles) from the MFFBAS API. More information on the Standard Consumption Profiles can be found [here](https://www.mffbas.nl/documenten/).

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import PythonMFFBASSource

    sjv_source = PythonMFFBASSource(
       start="2024-01-01",
       end="2024-01-02"
    )

    sjv_source.read_batch()
    ```

    Args:
       start (str): Start date in the format YYYY-MM-DD
       end (str): End date in the format YYYY-MM-DD

    !!! note "Note"
        It is not possible to collect fractions over a period before 2023-04-01 with this API. Requests are limited to a maximum of 31 days at a time.

    """
"""
        Attributes:
              SystemType (Environment): Requires Python
        """
"""
        Reads batch from the MFFBAS API.
        """
"""
        Raises:
              NotImplementedError: MFFBAS connector does not support the stream operation.
        """