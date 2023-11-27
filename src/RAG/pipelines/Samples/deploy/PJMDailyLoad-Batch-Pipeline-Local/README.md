# MISO Pipeline using RTDIP
This article provides a guide on how to execute a MISO pipeline using RTDIP. This pipeline was tested on an M2 Macbook Pro using VS Code in a Conda (3.11) environment.

## Prerequisites
This pipeline assumes you have a valid API key from [PJM](https://apiportal.pjm.com/) and have followed the installation instructions as specified in the Getting Started section. In particular ensure you have installed the following:

* [RTDIP SDK](../../../../getting-started/installation.md#installing-the-rtdip-sdk)

* [Java](../../../../getting-started/installation.md#java)

!!! note "RTDIP SDK Installation"
    Ensure you have installed the RTDIP SDK as follows:
    ```
    pip install "rtdip-sdk[pipelines,pyspark]"
    ```

## Components
|Name|Description|
|---------------------------|----------------------|
|[PJMDailyLoadISOSource](../../../code-reference/pipelines/sources/spark/iso/pjm_daily_load_iso.md)|Read daily load data from MISO API.|
|[PJMToMDMTransformer](../../../code-reference/pipelines/transformers/spark/iso/pjm_to_mdm.md)|Converts PJM Raw data into Meters Data Model.|
|[SparkDeltaDestination](../../../code-reference/pipelines/destinations/spark/delta.md)|Writes to a Delta table.|

## Example
Below is an example of how to set up a pipeline to read daily load data from the PJM API, transform it into the Meters Data Model and write it to a Delta table.
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/PJMDailyLoad-Batch-Pipeline-Local/pipeline.py:6:"
```

!!! note "Using environments"
    If using an environment, include the following lines at the top of your script to prevent a difference in Python versions in worker and driver:
    ```python
    --8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/PJMDailyLoad-Batch-Pipeline-Local/pipeline.py::5"
    ```