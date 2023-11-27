# Fledge Pipeline using Dagster and Databricks Connect

This article provides a guide on how to deploy a pipeline in dagster using the RTDIP SDK and Databricks Connect. This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.10) environment.

!!! note "Note"
    Reading from Eventhubs is currently not supported on Databricks Connect.

## Prerequisites
Deployment using Databricks Connect requires:

* a Databricks workspace

* a cluster in the same workspace

* a personal access token

Further information on Databricks requirements can be found [here](https://docs.databricks.com/en/dev-tools/databricks-connect-ref.html#requirements).


This pipeline job requires the packages:

* [rtdip-sdk](../../../../../getting-started/installation.md#installing-the-rtdip-sdk)

* [databricks-connect](https://pypi.org/project/databricks-connect/)

* [dagster](https://docs.dagster.io/getting-started/install)


!!! note "Dagster Installation"
    For Mac users with an M1 or M2 chip, installation of dagster should be done as follows:
    ```
    pip install dagster dagster-webserver --find-links=https://github.com/dagster-io/build-grpcio/wiki/Wheels
    ```

## Components
|Name|Description|
|---------------------------|----------------------|
|[SparkDeltaSource](../../../../code-reference/pipelines/sources/spark/delta.md)|Read data from a Delta table.|
|[BinaryToStringTransformer](../../../../code-reference/pipelines/transformers/spark/binary_to_string.md)|Converts a Spark DataFrame column from binary to string.|
|[FledgeOPCUAJsonToPCDMTransformer](../../../../code-reference/pipelines/transformers/spark/fledge_opcua_json_to_pcdm.md)|Converts a Spark DataFrame column containing a json string to the Process Control Data Model.|
|[SparkDeltaDestination](../../../../code-reference/pipelines/destinations/spark/delta.md)|Writes to a Delta table.|

## Authentication
For Databricks authentication, the following fields should be added to a configuration profile in your [`.databrickscfg`](https://docs.databricks.com/en/dev-tools/auth.html#config-profiles) file:

```
[PROFILE]
host = https://{workspace_instance}
token = dapi...
cluster_id = {cluster_id}
```

This profile should match the configurations in your `DatabricksSession` in the example below as it will be used by the [Databricks extension](https://docs.databricks.com/en/dev-tools/vscode-ext-ref.html#configure-the-extension) in VS Code for authenticating your Databricks cluster.

## Example
Below is an example of how to set up a pipeline to read Fledge data from a Delta table, transform it to RTDIP's [PCDM model](../../../../../domains/process_control/data_model.md) and write it to a Delta table.

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/Fledge-Dagster-Pipeline-Databricks/pipeline.py"
```

## Deploy
The following command deploys the pipeline to dagster:
`dagster dev -f <path/to/file.py>`

Using the link provided from the command above, click on Launchpad and hit run to run the pipeline.