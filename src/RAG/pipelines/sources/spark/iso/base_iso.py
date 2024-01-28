"""
    Base class for all the ISO Sources. It provides common functionality and helps in reducing the code redundancy.

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations
    """
"""
        Gets data from external ISO API.

        Args:
            url_suffix: String to be used as suffix to iso url.

        Returns:
            Raw content of the data received.

        """
"""
        Converts string datetime into Python datetime object with configured format and timezone.
        Args:
            datetime_str: String to be converted into datetime.

        Returns: Timezone aware datetime object.

        """
"""
        Hits the fetch_from_url method with certain parameters to get raw data from API.

        All the children ISO classes must override this method and call the fetch_url method
        in it.

        Returns:
             Raw DataFrame from API.
        """
"""
        Performs all the basic transformations to prepare data for further processing.
        All the children ISO classes must override this method.

        Args:
            df: Raw DataFrame, received from the API.

        Returns:
             Modified DataFrame, ready for basic use.

        """
"""
        Another data transformation helper method to be called after prepare data.
        Used for advance data processing such as cleaning, filtering, restructuring.
        All the children ISO classes must override this method if there is any post-processing required.

        Args:
            df: Initial modified version of DataFrame, received after preparing the data.

        Returns:
             Final version of data after all the fixes and modifications.

        """
"""
        Entrypoint method to return the final version of DataFrame.

        Returns:
            Modified form of data for specific use case.

        """
"""
        Performs all the options checks. Raises exception in case of any invalid value.
        Returns:
             True if all checks are passed.

        """
"""
        Ensures all the required options are provided and performs other validations.
        Returns:
             True if all checks are passed.

        """
"""
        Spark entrypoint, It executes the entire process of pulling, transforming & fixing data.
        Returns:
             Final Spark DataFrame converted from Pandas DataFrame post-execution.

        """
"""
        By default, the streaming operation is not supported but child classes can override if ISO supports streaming.

        Returns:
             Final Spark DataFrame after all the processing.

        """