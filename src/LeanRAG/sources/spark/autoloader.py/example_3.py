"""
        Raises:
            NotImplementedError: Auto Loader only supports streaming reads. To perform a batch read, use the read_stream method of this component and specify the Trigger on the write_stream to be `availableNow` to perform batch-like reads of cloud storage files.
        """