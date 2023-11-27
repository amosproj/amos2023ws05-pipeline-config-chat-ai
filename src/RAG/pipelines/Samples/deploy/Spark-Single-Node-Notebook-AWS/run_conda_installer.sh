#!/usr/bin/env bash
# Dependencies: x86_64 Architecture, Linux (Tested on Ubuntu >= 20.04 LTS) curl, unzip
start_time=`date +%s`
echo "PATH: $PATH"
CONDA_CHECK_CMD="conda"
CONDA_CMD_DESCRIPTION=$CONDA_CHECK_CMD
CONDA_INSTALLER_NAME="Miniconda3-latest-Linux-x86_64.sh"
CONDA_INSTALLER_URL="https://repo.anaconda.com/miniconda/$CONDA_INSTALLER_NAME"
DEPLOYER_TMP_DIR=$(echo ${TMPDIR:-/tmp}"/DEPLOYER")
MINICONDA_NAME=miniconda
MINICONDA_PATH=$HOME/$MINICONDA_NAME/
PATH=$MINICONDA_PATH/bin:$PATH
CONDA_ENV="rtdip-sdk"
CONDA_ENV_HOME=$(pwd)/apps/$CONDA_ENV
mkdir -p $CONDA_ENV_HOME
CWD=$(pwd)
echo "Current Working Directory: $CWD"
echo "CONDA ENV HOME: $CONDA_ENV_HOME"
echo "DEPLOYER TMP Dir: $DEPLOYER_TMP_DIR"
if ! command -v $CONDA_CHECK_CMD &> /dev/null
then
    echo "Current dir:"
    echo "$CONDA_CMD_DESCRIPTION could not be found. Going to Install it"
    mkdir -p $DEPLOYER_TMP_DIR
    echo "Working Dir to download conda:"
    cd $DEPLOYER_TMP_DIR
    pwd
    curl -O --url $CONDA_INSTALLER_URL
    chmod +x $DEPLOYER_TMP_DIR/*.sh
    bash $CONDA_INSTALLER_NAME -b -p $HOME/miniconda
fi
cd $CONDA_ENV_HOME
echo "Current Dir:"
pwd

echo "Updating Conda"
conda update -n base conda -y
echo "Installing Mamba Solver"
conda install -n base conda-libmamba-solver -y
echo "Setting Solver to libmama"
conda config --set solver libmamba



echo "Creating Conda Environment"
conda  env create -f environment.yml -y

#
# JDK
echo "Installing JDK jdk-17.0.2 ***********************************"
export JAVA_VERSION="jdk-17.0.2"
export JDK_FILE_NAME="openjdk-17.0.2_linux-x64_bin.tar.gz"
export JDK_DOWNLOAD_URL="https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/$JDK_FILE_NAME"

if [ -f "$CONDA_ENV/$JDK_FILE_NAME" ]; then
  echo "$CONDA_ENV/$JDK_FILE_NAME Exists"
  echo "Removing JDK: $JDK_FILE_NAME"
  rm -rf $CONDA_ENV/$JAVA_VERSION
  # rm $CONDA_ENV/$JDK_FILE_NAME
  unlink $HOME/JDK
fi

if test -f "$JDK_FILE_NAME";
then
  echo "$JDK_FILE_NAME exists"
else
  echo "$JDK_FILE_NAME does not exists. Downloading it from $JDK_DOWNLOAD_URL"
  curl -o $JDK_FILE_NAME $JDK_DOWNLOAD_URL
fi

tar xvfz $JDK_FILE_NAME > /dev/null
ln -s $CONDA_ENV_HOME/$JAVA_VERSION $HOME/JDK
export JAVA_HOME=$HOME/JDK
export PATH=$HOME/JDK/bin:$PATH

# SPARK 3.3.2
echo "Installing SPARK 3.3.2 ***********************************" 
export SPARK_VERSION="spark-3.3.2-bin-hadoop3"
export SPARK_FILE_NAME="spark-3.3.2-bin-hadoop3.tgz"
export SPARK_DOWNLOAD_URL="https://archive.apache.org/dist/spark/spark-3.3.2/$SPARK_FILE_NAME"
export PYSPARK_VERSION="3.3.2"


if [ -f "$CONDA_ENV/$SPARK_VERSION" ]; then
  echo "$CONDA_ENV/$SPARK_FILE_NAME Exists"
  echo "Removing Spark: $SPARK_FILE_NAME"
  rm -rf $CONDA_ENV/$SPARK_VERSION
  # rm $CONDA_ENV/$SPARK_FILE_NAME
  unlink $HOME/SPARK
fi

if test -f "$SPARK_FILE_NAME";
then
  echo "$SPARK_FILE_NAME exists"
else
  echo "$SPARK_FILE_NAME does not exists. Downloading it from $SPARK_DOWNLOAD_URL"
  curl -o $SPARK_FILE_NAME $SPARK_DOWNLOAD_URL
fi


tar xvfz $SPARK_FILE_NAME > /dev/null
ln -s $CONDA_ENV_HOME/$SPARK_VERSION $HOME/SPARK
export SPARK_HOME=$HOME/SPARK


# Extra libraries
echo "Installing Extra Libs ***********************************"
export AWS_JAVA_SDK_BUNDLE_JAR_FILE_NAME="aws-java-sdk-bundle-1.11.1026.jar"
export AWS_JAVA_SDK_BUNDLE_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.1026/$AWS_JAVA_SDK_BUNDLE_JAR_FILE_NAME"

export HADOOP_AWS_JAR_FILE_NAME="hadoop-aws-3.3.2.jar"
export HADOOP_AWS_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.2/$HADOOP_AWS_JAR_FILE_NAME"

export HADOOP_COMMON_JAR_FILE_NAME="hadoop-common-3.3.2.jar"
export HADOOP_COMMON_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.3.2/$HADOOP_COMMON_JAR_FILE_NAME"

export HADOOP_HDFS_JAR_FILE_NAME="hadoop-hdfs-3.3.2.jar"
export HADOOP_HDFS_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-hdfs/3.3.2/$HADOOP_HDFS_JAR_FILE_NAME"

export WOODSTOCK_CORE_JAR_FILE_NAME="woodstox-core-6.5.1.jar"
export WOODSTOCK_CORE_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/com/fasterxml/woodstox/woodstox-core/6.5.1/$WOODSTOCK_CORE_JAR_FILE_NAME"

export STAX2_API_JAR_FILE_NAME="stax2-api-4.2.1.jar"
export STAX2_API__JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/org/codehaus/woodstox/stax2-api/4.2.1/$STAX2_API_JAR_FILE_NAME"

export COMMONS_CONFIGURATION_JAR_FILE_NAME="commons-configuration2-2.9.0.jar"
export COMMONS_CONFIGURATION_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/org/apache/commons/commons-configuration2/2.9.0/$COMMONS_CONFIGURATION_JAR_FILE_NAME"

export RE2J_JAR_FILE_NAME="re2j-1.7.jar"
export RE2J_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/com/google/re2j/re2j/1.7/$RE2J_JAR_FILE_NAME"

export AZURE_EVENTHUBS_SPARK_JAR_FILE_NAME="azure-eventhubs-spark_2.12-2.3.22.jar"
export AZURE_EVENTHUBS_SPARK_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/com/microsoft/azure/azure-eventhubs-spark_2.12/2.3.22/$AZURE_EVENTHUBS_SPARK_JAR_FILE_NAME"

export AZURE_EVENTHUBS_JAR_FILE_NAME="azure-eventhubs-3.3.0.jar"
export AZURE_EVENTHUBS_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/com/microsoft/azure/azure-eventhubs/3.3.0/$AZURE_EVENTHUBS_JAR_FILE_NAME"

export SCALA_JAVA8_COMPAT_JAR_FILE_NAME="scala-java8-compat_2.12-1.0.2.jar"
export SCALA_JAVA8_COMPAT_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/org/scala-lang/modules/scala-java8-compat_2.12/1.0.2/$SCALA_JAVA8_COMPAT_JAR_FILE_NAME"

export PROTON_J_JAR_FILE_NAME="proton-j-0.34.1.jar"
export PROTON_J_JAR_DOWNLOAD_URL="https://repo1.maven.org/maven2/org/apache/qpid/proton-j/0.34.1/$PROTON_J_JAR_FILE_NAME"

curl -o $AWS_JAVA_SDK_BUNDLE_JAR_FILE_NAME $AWS_JAVA_SDK_BUNDLE_JAR_DOWNLOAD_URL
mv $AWS_JAVA_SDK_BUNDLE_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $HADOOP_AWS_JAR_FILE_NAME $HADOOP_AWS_JAR_DOWNLOAD_URL
mv $HADOOP_AWS_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $HADOOP_COMMON_JAR_FILE_NAME $HADOOP_COMMON_JAR_DOWNLOAD_URL
mv $HADOOP_COMMON_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $HADOOP_HDFS_JAR_FILE_NAME $HADOOP_HDFS_JAR_DOWNLOAD_URL
mv $HADOOP_HDFS_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $WOODSTOCK_CORE_JAR_FILE_NAME $WOODSTOCK_CORE_JAR_DOWNLOAD_URL
mv $WOODSTOCK_CORE_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $STAX2_API_JAR_FILE_NAME $STAX2_API__JAR_DOWNLOAD_URL
mv  $STAX2_API_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $COMMONS_CONFIGURATION_JAR_FILE_NAME $COMMONS_CONFIGURATION_JAR_DOWNLOAD_URL
mv  $COMMONS_CONFIGURATION_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $RE2J_JAR_FILE_NAME $RE2J_JAR_DOWNLOAD_URL
mv  $RE2J_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $AZURE_EVENTHUBS_SPARK_JAR_FILE_NAME $AZURE_EVENTHUBS_SPARK_JAR_DOWNLOAD_URL
mv  $AZURE_EVENTHUBS_SPARK_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $AZURE_EVENTHUBS_JAR_FILE_NAME $AZURE_EVENTHUBS_JAR_DOWNLOAD_URL
mv  $AZURE_EVENTHUBS_JAR_FILE_NAME $SPARK_HOME/jars

curl -o $SCALA_JAVA8_COMPAT_JAR_FILE_NAME $SCALA_JAVA8_COMPAT_JAR_DOWNLOAD_URL
mv $SCALA_JAVA8_COMPAT_JAR_FILE_NAME  $SPARK_HOME/jars

curl -o $PROTON_J_JAR_FILE_NAME $PROTON_J_JAR_DOWNLOAD_URL
mv $PROTON_J_JAR_FILE_NAME $SPARK_HOME/jars

# Cleaning up
rm $SPARK_FILE_NAME
rm $JDK_FILE_NAME

#
echo "Finished INSTALLING $JAVA_VERSION and $SPARK_VERSION and Extra Libraries"

eval "$(conda shell.bash hook)"
conda config --set default_threads 4
conda env list
# Uncoment the line below to avoid error: CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
# source $HOME/$MINICONDA_NAME/etc/profile.d/conda.sh

conda activate $CONDA_ENV

conda info
end_time=`date +%s`
runtime=$((end_time-start_time))
echo "Total Installation Runtime: $runtime [seconds]"
# Creating env file
CONDA_ENVIRONMENT_FILE_NAME="conda_environment_$CONDA_ENV.sh"
echo "#!/usr/bin/env bash" > $CONDA_ENVIRONMENT_FILE_NAME
echo "export PATH=$PATH" >> $CONDA_ENVIRONMENT_FILE_NAME
echo "export JAVA_HOME=$JAVA_HOME" >> $CONDA_ENVIRONMENT_FILE_NAME
echo "export SPARK_HOME=$SPARK_HOME" >> $CONDA_ENVIRONMENT_FILE_NAME
echo "source $HOME/$MINICONDA_NAME/etc/profile.d/conda.sh" >> $CONDA_ENVIRONMENT_FILE_NAME
chmod +x $CONDA_ENVIRONMENT_FILE_NAME
echo "export SPARK_HOME=$SPARK_HOME"
if [ -z ${NOTEBOOK_PORT+x} ]; then NOTEBOOK_PORT="8080"; else echo "NOTEBOOK_PORT: $NOTEBOOK_PORT"; fi
echo "NOTEBOOK_PORT: $NOTEBOOK_PORT"
source ./$CONDA_ENVIRONMENT_FILE_NAME
jupyter notebook --no-browser --port=$NOTEBOOK_PORT --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''  --allow-root
