"""
    Base class for extracting forecast data downloaded in .nc format from ECMWF MARS Server.

    Args:
        load_path (str): Path to local directory where the nc files will be stored, in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        run_frequency (str):Frequency format of runs to download, e.g. "H"
        run_interval (str): Interval of runs, e.g. a run_frequency of "H" and run_interval of "12" will extract the data of the 00 and 12 run for each day.
        lat (DataArray): Latitude values to extract from nc files
        lon (DataArray): Longitude values to extract from nc files
        utc (bool = True): Whether to convert the time to UTC or not
    """