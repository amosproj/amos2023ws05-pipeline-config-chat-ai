# Spark Single Node Notebook AWS

This article provides a guide how to create a conda based self contained environment to run RTDIP that integrates the following components:
* Java and Spark (Single node configuration). Currently v3.3.2 Spark has been configured
* AWS Libraries for Spark/Hadoop v3.3.2
* Jupyter Notebook 
* RTDIP (v0.6.1)


The components of this environment are pinned to specific versions.

## Prerequisites
The prerequisites for running the environment are:

* run_conda_installer.sh: An x86 Linux environment with enough free space (Tested on Linux Ubuntu 22.04. A clean environment is preferred)
* the installer will run Jupyter notebook on port 8080. Check that this port is free or change the configuration in the installer.

# Deploy and Running
Run *run_conda_installer.sh*. After the installer completes:
* A new file *conda_environment_rtdip-sdk.sh* is created. Please use this file (e.g. *source ./conda_environment_rtdip-sdk.sh*)  to activate the conda environment.
* On http://host:8080/ where host is the machine where the installer was run, a jupyter notebook server will be running. Notebooks can be created to run for example RTDIP pipelines.

