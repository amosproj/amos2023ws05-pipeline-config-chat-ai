"""
    Executes Pipeline components in their intended order as a complete data pipeline. It ensures that components dependencies are injected as needed.

    Parameters:
        job (PipelineJob): Contains the steps and tasks of a PipelineJob to be executed
        batch_job (bool): Specifies if the job is to be executed as a batch job
    """
"""
        Orders tasks within a job
        """
"""
        Orders steps within a task
        """
"""
        Determines the dependencies to be injected into each component
        """
"""
        Executes all the steps and tasks in a pipeline job as per the job definition.
        """