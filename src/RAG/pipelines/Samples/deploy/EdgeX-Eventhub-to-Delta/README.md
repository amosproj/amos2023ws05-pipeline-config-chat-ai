# EdgeX Eventhub to Delta Pipeline

This article provides a guide on how to execute a pipeline that batch reads EdgeX data from an Eventhub and writes to a Delta Table locally using the RTDIP SDK. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.10) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../getting-started/installation.md#installing-the-rtdip-sdk)


## Components
|Name|Description|
|---------------------------|----------------------|
|[SparkEventhubSource](../../../code-reference/pipelines/sources/spark/eventhub.md)|Reads data from an Eventhub.|
|[BinaryToStringTransformer](../../../code-reference/pipelines/transformers/spark/binary_to_string.md)|Transforms Spark DataFrame column to string.|
|[EdgeXOPCUAJsonToPCDMTransformer](../../../code-reference/pipelines/transformers/spark/edgex_opcua_json_to_pcdm.md)|Transforms EdgeX to PCDM.|
|[SparkDeltaDestination](../../../code-reference/pipelines/destinations/spark/delta.md)|Writes to Delta.|

## Common Errors
|Error|Solution|
|---------------------------|----------------------|
|[com.google.common.util.concurrent.ExecutionError: java.lang.NoClassDefFoundError: org/apache/spark/ErrorClassesJsonReader]|The Delta version in the Spark Session must be compatible with your local Pyspark version. See [here](https://docs.delta.io/latest/releases.html){ target="_blank" } for version compatibility|



## Example
Below is an example of how to read from and write to Delta Tables locally without the need for Spark

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/EdgeX-Eventhub-to-Delta/pipeline.py"
```