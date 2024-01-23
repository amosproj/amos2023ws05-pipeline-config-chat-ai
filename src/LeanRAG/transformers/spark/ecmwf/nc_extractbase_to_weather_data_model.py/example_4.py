"""Extract raw data from stored nc filed downloaded via ECMWF MARS.

        Args:
            tag_prefix (str): Prefix of the tag names of raw tags to be added to the dataframe
            variables (list): List of variable names of raw tags to be extracted from the nc files
            method (str, optional): The method used to match latitude/longitude in xarray using .sel(), by default "nearest"

        Returns:
            df (pd.DataFrame): Raw data extracted with lat, lon, run_time, target_time as a pd.multiindex and variables as columns.
        """