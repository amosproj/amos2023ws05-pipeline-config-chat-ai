# Python Delta Local Pipeline

This article provides a guide on how to execute a simple Delta Table copy locally without Spark using the RTDIP SDK. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.10) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../getting-started/installation.md#installing-the-rtdip-sdk)


## Components
|Name|Description|
|---------------------------|----------------------|
|[PythonDeltaSource](../../../code-reference/pipelines/sources/python/delta.md)|Reads data from a Delta Table.|
|[PythonDeltaDestination](../../../code-reference/pipelines/destinations/python/delta.md)|Writes to a Delta table.|

## Example
Below is an example of how to read from and write to Delta Tables locally without the need for Spark

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/Python-Delta-to-Delta/pipeline.py"
```