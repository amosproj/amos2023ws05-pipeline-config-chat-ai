# Fledge Eventhub to Honeywell APM Eventhub Pipeline

This article provides a guide on how to execute a pipeline that batch reads Fledge data from an Eventhub, transforms to APM and writes to another Eventhub using the RTDIP SDK. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.10) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../getting-started/installation.md#installing-the-rtdip-sdk)


## Components
|Name|Description|
|---------------------------|----------------------|
|[SparkEventhubSource](../../../code-reference/pipelines/sources/spark/eventhub.md)|Reads data from an Eventhub.|
|[BinaryToStringTransformer](../../../code-reference/pipelines/transformers/spark/binary_to_string.md)|Transforms Spark DataFrame column to string.|
|[FledgeOPCUAJsonToPCDMTransformer](../../../code-reference/pipelines/transformers/spark/fledge_opcua_json_to_pcdm.md)|Transforms Fledge to PCDM.|
|[SparkEventhubDestination](../../../code-reference/pipelines/destinations/spark/eventhub.md)|Writes to an Eventhub.|


## Example
Below is an example of reading from an Eventhub, transforming and writing to another Eventhub

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/Fledge-Eventhub-to-HW_APM-eventhub/pipeline.py"
```