"""
    Download nc files from ECMWF MARS server using the ECMWF python API.
    Data is downloaded in parallel using joblib from ECMWF MARS server using the ECMWF python API.

    Parameters:
        save_path (str): Path to local directory where the nc files will be stored, in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        ecmwf_api_key (str): API key for ECMWF MARS server
        ecmwf_api_email (str): Email for ECMWF MARS server
        ecmwf_api_url (str): URL for ECMWF MARS server
        run_frequency (str):Frequency format of runs to download, e.g. "H"
        run_interval (str): Interval of runs, e.g. a run_frequency of "H" and run_interval of "12" will extract the data of the 00 and 12 run for each day.
    """