"""Extract a grid from a local .nc file downloaded from ECMWF via MARS

    Args:
        lat_min (float): Minimum latitude of grid to extract
        lat_max (float): Maximum latitude of grid to extract
        lon_min (float): Minimum longitude of grid to extract
        lon_max (float): Maximum longitude of grid to extract
        grid_step (float): The grid length to use to define the grid, e.g. 0.1.
        load_path (str): Path to local directory with nc files downloaded in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        run_frequency (str): Frequency format of runs to download, e.g. "H"
        run_interval (str): Interval of runs, e.g. a run_frequency of "H" and run_interval of "12" will extract the data of the 00 and 12 run for each day.
        utc (bool, optional): Add utc to the datetime indexes? Defaults to True.

    """