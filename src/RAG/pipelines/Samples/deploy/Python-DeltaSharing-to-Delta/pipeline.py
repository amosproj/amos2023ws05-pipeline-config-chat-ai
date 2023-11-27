from rtdip_sdk.pipelines.sources.python.delta_sharing import PythonDeltaSharingSource
from rtdip_sdk.pipelines.destinations.python.delta import PythonDeltaDestination

source = PythonDeltaSharingSource("{/path/to/config/credential/file}","{name_of_share}", "{schema_name}", "{table_name}").read_batch()

destination = PythonDeltaDestination(source, "{/path/to/table}", mode="append").write_batch()