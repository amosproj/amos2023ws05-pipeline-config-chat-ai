# Python Delta Sharing Local Pipeline

This article provides a guide on how to execute a simple Delta Sharing Table read and local write without Spark using the RTDIP SDK. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.10) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../getting-started/installation.md#installing-the-rtdip-sdk)


## Components
|Name|Description|
|---------------------------|----------------------|
|[PythonDeltaSharingSource](../../../code-reference/pipelines/sources/python/delta_sharing.md)|Reads data from a Delta Table with Delta Sharing enabled.|
|[PythonDeltaDestination](../../../code-reference/pipelines/destinations/python/delta.md)|Writes to a Delta table.|

## Example
Below is an example of how to read from a table with Delta Sharing and write to Delta locally without the need for Spark

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/Python-Delta-to-Delta/pipeline.py"
```