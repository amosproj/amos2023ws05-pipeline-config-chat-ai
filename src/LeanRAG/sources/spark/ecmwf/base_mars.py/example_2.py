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