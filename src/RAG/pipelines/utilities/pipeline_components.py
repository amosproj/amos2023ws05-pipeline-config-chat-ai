"""
    Gets the list of imported RTDIP components. Returns the libraries and settings of the components to be used in the pipeline.

    Call this component after all imports of the RTDIP components to ensure that the components can be determined.

    Parameters:
        module (optional str): Provide the module to use for imports of rtdip-sdk components. If not populated, it will use the calling module to check for imports
        spark_config (optional dict): Additional spark configuration to be applied to the spark session
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """