# MISO Pipeline using RTDIP and Databricks
This article provides a guide on how to deploy a MISO pipeline from a local file to a Databricks workflow using the RTDIP SDK and was tested on an M2 Macbook Pro using VS Code in a Conda (3.11) environment. RTDIP Pipeline Components provide Databricks with all the required Python packages and JARs to execute each component, this will automatically be set up during workflow creation.

## Prerequisites
This pipeline assumes you have a Databricks workspace and have followed the installation instructions as specified in the Getting Started section. In particular ensure you have installed the following:

* [RTDIP SDK](../../../../../getting-started/installation.md#installing-the-rtdip-sdk)

* [Java](../../../../../getting-started/installation.md#java)

!!! note "RTDIP SDK Installation"
    Ensure you have installed the RTDIP SDK as follows:
    ```
    pip install "rtdip-sdk[pipelines]"
    ```

## Components
|Name|Description|
|---------------------------|----------------------|
|[MISODailyLoadISOSource](../../../../code-reference/pipelines/sources/spark/iso/miso_daily_load_iso.md)|Read daily load data from MISO API.|
|[MISOToMDMTransformer](../../../../code-reference/pipelines/transformers/spark/iso/miso_to_mdm.md)|Converts MISO Raw data into Meters Data Model.|
|[SparkDeltaDestination](../../../../code-reference/pipelines/destinations/spark/delta.md)|Writes to a Delta table.|
|[DatabricksSDKDeploy](../../../../code-reference/pipelines/deploy/databricks.md)|Deploys an RTDIP Pipeline to Databricks Workflows leveraging the Databricks [SDK.](https://docs.databricks.com/dev-tools/sdk-python.html)|
|[DeltaTableOptimizeUtility](../../../../code-reference/pipelines/utilities/spark/delta_table_optimize.md)|[Optimizes](https://docs.delta.io/latest/optimizations-oss.html) a Delta Table|
|[DeltaTableVacuumUtility](../../../../code-reference/pipelines/utilities/spark/delta_table_vacuum.md)|[Vacuums](https://docs.delta.io/latest/delta-utility.html#-delta-vacuum) a Delta Table|

## Example
Below is an example of how to set up a pipeline job to read daily load data from the MISO API, transform it into the Meters Data Model and write it to a Delta table.
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/MISODailyLoad-Batch-Pipeline-Databricks/pipeline.py"
```

## Maintenance
The RTDIP SDK can be used to maintain Delta tables in Databricks, an example of how to set up a maintenance job to optimize and vacuum the MISO tables written from the previous example is provided below.
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/MISODailyLoad-Batch-Pipeline-Databricks/maintenance.py"
```

## Deploy
Deployment to Databricks uses the Databricks [SDK](https://docs.databricks.com/en/dev-tools/sdk-python.html). Users have the option to control the job's configurations including the cluster and schedule.
```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/MISODailyLoad-Batch-Pipeline-Databricks/deploy.py"
```