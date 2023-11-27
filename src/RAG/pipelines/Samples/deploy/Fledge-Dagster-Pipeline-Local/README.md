# Fledge Pipeline using Dagster

This article provides a guide on how to deploy a pipeline in dagster using the RTDIP SDK. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.10) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../../getting-started/installation.md#installing-the-rtdip-sdk)

* [dagster](https://docs.dagster.io/getting-started/install)


!!! note "Dagster Installation"
    For Mac users with an M1 or M2 chip, installation of dagster should be done as follows:
    ```
    pip install dagster dagster-webserver --find-links=https://github.com/dagster-io/build-grpcio/wiki/Wheels
    ```

## Components
|Name|Description|
|---------------------------|----------------------|
|[SparkEventhubSource](../../../../code-reference/pipelines/sources/spark/eventhub.md)|Read data from an Eventhub.|
|[BinaryToStringTransformer](../../../../code-reference/pipelines/transformers/spark/binary_to_string.md)|Converts a Spark DataFrame column from binary to string.|
|[FledgeOPCUAJsonToPCDMTransformer](../../../../code-reference/pipelines/transformers/spark/fledge_opcua_json_to_pcdm.md)|Converts a Spark DataFrame column containing a json string to the Process Control Data Model.|
|[SparkDeltaDestination](../../../../code-reference/pipelines/destinations/spark/delta.md)|Writes to a Delta table.|

## Example
Below is an example of how to set up a pipeline to read Fledge data from an Eventhub, transform it to RTDIP's [PCDM model](../../../../../domains/process_control/data_model.md) and write it to a Delta table on your machine.

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/Fledge-Dagster-Pipeline-Local/pipeline.py"
```

## Deploy
The following command deploys the pipeline to dagster:
`dagster dev -f <path/to/file.py>`

Using the link provided from the command above, click on Launchpad and hit run to run the pipeline.