# ECMWF to Delta Pipeline

This article provides a guide on how to execute a pipeline that makes an API request to pull the ECMWF MARS Data as a .nc file, transform the .nc file to a dataframe from a grid range and writes to a Delta Table locally using the RTDIP SDK. 

This pipeline was tested on an M2 Macbook Pro using VS Code in a Python (3.11) environment.

## Prerequisites
This pipeline job requires the packages:

* [rtdip-sdk](../../../../getting-started/installation.md#installing-the-rtdip-sdk)


## Components
|Name|Description|
|---------------------------|----------------------|
|[SparkECMWFWeatherForecastSource](../../../code-reference/pipelines/sources/spark/ecmwf/weather_forecast.md)|Pulls data from ECMWF MARS API and stores as a .nc file.|
|[ECMWFExtractGridToWeatherDataModel](../../../code-reference/pipelines/transformers/spark/ecmwf/nc_extractgrid_to_weather_data_model.md)|Transforms ECMWF .nc file to a dataframe ingesting Grid Data.|
|[SparkDeltaDestination](../../../code-reference/pipelines/destinations/spark/delta.md)|Writes to Delta.|

## Common Errors
|Error|Solution|
|---------------------------|----------------------|
|[com.google.common.util.concurrent.ExecutionError: java.lang.NoClassDefFoundError: org/apache/spark/ErrorClassesJsonReader]|The Delta version in the Spark Session must be compatible with your local Pyspark version. See [here](https://docs.delta.io/latest/releases.html){ target="_blank" } for version compatibility|



## Example
Below is an example of how to read from and write to Delta Tables locally without the need for Spark

```python
--8<-- "https://raw.githubusercontent.com/rtdip/samples/main/pipelines/deploy/ECMWF-to-Delta/pipeline.py"
```