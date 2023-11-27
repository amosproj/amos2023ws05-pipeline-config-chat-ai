# Honeywell APM Eventhub to PCDM Delta Pipeline

This article provides a guide on how to execute a pipeline that batch reads HW APM data from an Eventhub, transforms to PCDM and writes to Delta using the RTDIP SDK. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.10) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../getting-started/installation.md#installing-the-rtdip-sdk)


## Components
|Name|Description|
|---------------------------|----------------------|
|[SparkEventhubSource](../../../code-reference/pipelines/sources/spark/eventhub.md)|Reads data from an Eventhub.|
|[BinaryToStringTransformer](../../../code-reference/pipelines/transformers/spark/binary_to_string.md)|Transforms Spark DataFrame column to string.|
|[HoneywellAPMJsonToPCDMTransformer](../../../code-reference/pipelines/transformers/spark/honeywell_apm_to_pcdm.md)|Transforms HW APM to PCDM.|
|[SparkPCDMToDeltaDestination](../../../code-reference/pipelines/destinations/spark/pcdm_to_delta.md)|Writes to Delta.|


## Example
Below is an example of reading from an Eventhub, transforming to PCDM and writing to Delta

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/HW_APM-Eventhub-to-pcdm-Delta/pipeline.py"
```