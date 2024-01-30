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
"""Retrieve the data from the server.

        Function will use the ecmwf api to download the data from the server.
        Note that mars has a max of two active requests per user and 20 queued
        requests.
        Data is downloaded in parallel using joblib from ECMWF MARS server using the ECMWF python API.


        Parameters:
            mars_dict (dict): Dictionary of mars parameters.
            n_jobs (int, optional): Download in parallel? by default None, i.e. no parallelization
            backend (str, optional) : Specify the parallelization backend implementation in joblib, by default "loky"
            tries (int, optional): Number of tries for each request if it fails, by default 5
            cost (bool, optional):  Pass a cost request to mars to estimate the size and efficiency of your request,
                but not actually download the data. Can be useful for defining requests,
                by default False.
        """
"""
        Return info on each ECMWF request.

        Returns:
            pd.Series: Successful request for each run == 1.
        """