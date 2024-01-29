"""
    Converts a json string into a Pipeline Job.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.secrets import PipelineJobFromJsonConverter

    convert_json_string_to_pipline_job = PipelineJobFromJsonConverter(
        pipeline_json = "{JSON-STRING}"
    )

    convert_json_string_to_pipline_job.convert()
    ```

    Parameters:
        pipeline_json (str): Json representing PipelineJob information, including tasks and related steps
    """
"""
        Converts a json string to a Pipeline Job
        """
"""
    Converts a Pipeline Job into a json string.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.secrets import PipelineJobToJsonConverter

    convert_pipeline_job_to_json_string = PipelineJobFromJsonConverter(
        pipeline_json = PipelineJob
    )

    convert_pipeline_job_to_json_string.convert()
    ```

    Parameters:
        pipeline_job (PipelineJob): A Pipeline Job consisting of tasks and steps
    """
"""
        Converts a Pipeline Job to a json string
        """