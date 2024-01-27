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
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Converts the tag names of wind speed from the format used in the nc files to the format used in the weather data model.

        Args:
            x (list): List of variable names of raw tags to be extracted from the nc files

        Returns:
            new_tags(list): List of variable names of raw tags to be extracted from the nc files, converted to the format used in the weather data model.
        """
"""Extract raw data from stored nc filed downloaded via ECMWF MARS.

        Args:
            tag_prefix (str): Prefix of the tag names of raw tags to be added to the dataframe
            variables (list): List of variable names of raw tags to be extracted from the nc files
            method (str, optional): The method used to match latitude/longitude in xarray using .sel(), by default "nearest"

        Returns:
            df (pd.DataFrame): Raw data extracted with lat, lon, run_time, target_time as a pd.multiindex and variables as columns.
        """