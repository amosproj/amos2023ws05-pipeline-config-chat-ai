from rtdip_sdk.pipelines.sources.spark.ecmwf.weather_forecast import SparkECMWFWeatherForecastSource
from rtdip_sdk.pipelines.transformers.spark.ecmwf.nc_extractgrid_to_weather_data_model import ECMWFExtractGridToWeatherDataModel
from rtdip_sdk.pipelines.destinations.spark.delta import SparkDeltaDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility


ecmwf_api_key = "xxxxx"
ecmwf_api_email = "xxxxx"

date_start = "2020-10-01 00:00:00"
date_end = "2020-10-02 00:00:00"

ecmwf_class = "od"
stream = "oper"
expver = "1"
leveltype = "sfc"
run_interval = "12"
run_frequency = "H"
grid_step = 0.1
ec_vars = [
    "cbh", "dsrp", "sp", "tcwv", "tcc"
]

tag_prefix = "US:[55, -130, 20, -60]:"
method = "nearest"
path = '/dbfs/forecast/nc/US/' # Path to save the data can be changed
forecast_area = [55, -130, 20, -60]  # N/W/S/E
lat_max = 50
lat_min = 25
lon_max = -65
lon_min = -75


def pipeline():

    spark = SparkSessionUtility(config={}).execute()


    weather_source = SparkECMWFWeatherForecastSource(
        spark=spark,
        date_start=date_start,
        date_end=date_end,
        save_path=path,
        ecmwf_class=ecmwf_class,
        stream=stream,
        expver=expver,
        leveltype=leveltype,
        ec_vars=ec_vars,
        forecast_area=forecast_area,
        ecmwf_api_key=ecmwf_api_key,
        ecmwf_api_email=ecmwf_api_email,
    )
    
    weather_source.read_batch()
        
    extract = ECMWFExtractGridToWeatherDataModel(
            lat_min=lat_min,
            lat_max=lat_max,
            lon_min=lon_min,
            lon_max=lon_max,
            grid_step=grid_step,
            load_path=path,
            date_start=date_start,
            date_end=date_end,
            run_interval=run_interval,
            run_frequency=run_frequency
    )

    df = extract.transform(tag_prefix, ec_vars, method)

    sparkdf = spark.createDataFrame(df) 

    SparkDeltaDestination(
        data=sparkdf, options={}, destination="{path/to/table}"
    ).write_batch()


if __name__ == "__main__":
    pipeline()

