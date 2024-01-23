"""
    The Weather Forecast API V1 Source class to doownload nc files from ECMWF MARS server using the ECMWF python API.

    Parameters:
        spark (SparkSession): Spark Session instance
        save_path (str): Path to local directory where the nc files will be stored, in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format    date_end:str,
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        ecmwf_class (str): ecmwf classification of data
        stream (str): Operational model stream
        expver (str): Version of data
        leveltype (str): Surface level forecasts
        ec_vars (list): Variables of forecast measurements.
        forecast_area (list): N/W/S/E coordinates of the forecast area
        ecmwf_api_key (str): API key for ECMWF API
        ecmwf_api_email (str): Email for ECMWF API
    """