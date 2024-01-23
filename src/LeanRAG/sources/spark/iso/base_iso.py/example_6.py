"""
        Another data transformation helper method to be called after prepare data.
        Used for advance data processing such as cleaning, filtering, restructuring.
        All the children ISO classes must override this method if there is any post-processing required.

        Args:
            df: Initial modified version of DataFrame, received after preparing the data.

        Returns:
             Final version of data after all the fixes and modifications.

        """