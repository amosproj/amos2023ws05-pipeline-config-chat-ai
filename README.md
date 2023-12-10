# Pipeline Configuration Chat AI (AMOS WS23)

<div style="text-align:center">
  <img src="https://github.com/amosproj/amos2023ws05-pipeline-config-chat-ai/raw/main/Deliverables/sprint-01/team-logo.PNG" alt="Team Logo" width="350"/>
</div>

## Project Mission 
This project is to develop a chat AI based user interface for the description and configuration of
RTDIP data pipelines. Users are to interact with the chat AI to create an RTDIP configuration,
consisting of a block configuration (the steps in the pipeline) and PySpark code for individual
blocks to perform the data processing. Chat history and generated output should be visible to the user in parallel, e.g. chat history to the left, generated code to the right.

## Meet the Team 
Scrum Master: [@SaraElBrak](https://github.com/SaraElBrak)  
Product Owners: [@AviKatziuk](https://github.com/AviKatziuk), [@ceciliabetb](https://github.com/ceciliabetb)  
Software Developers: [@lyndanajjar](https://github.com/lyndanajjar), [@bergzain](https://github.com/bergzain), [@Obismadi99](https://github.com/Obismadi99), [@Nahrain1](https://github.com/Nahrain1)

The planning document of the team is found [here](https://docs.google.com/spreadsheets/d/1m1z2m_p6k0ATw0RVNXJMbDp-RrOOPxpu0c3PPCtrwBI/edit#gid=6) 

## Prerequisites
Ensure that you have installed:

* Python version 3.11 or higher
* Docker Desktop 
* OpenAI API Key   

## Build Process 
To get started with this project, follow these steps: 

* Clone the github repository 
```
git clone https://github.com/amosproj/amos2023ws05-pipeline-config-chat-ai.git
``` 
* Install Dependencies 
To set up the required dependencies, create a virtual environment and run the following command:
```
pip install -r requirements.txt
```
* Run the Application with Docker
Navigate to the `src` folder by using: 

``` 
cd src 
```
Ensure that the Docker daemon is running before proceeding. Follow these steps to run the application:
Step 1: Build the Docker Image
Execute the following command to build the Docker image. Replace `<your-image-name>` with your chosen image name:

```
docker build -t <your-image-name> .
```
Step 2: Run the Docker Container
Launch the container using the following command, specifying port 8501 for Streamlit:

```
docker run -dp 8501:8501 <your-image-name>
```

Once the container is successfully running, access the application by clicking the link displayed in the `Ports` column within the Docker Desktop interface. This link corresponds to the port mapping configured during the container's launch and serves as the entry point to interact with the application.

_Note: Remember to replace <your-image-name> with the actual name you assigned to your Docker image._

* Accessing the Chatbot Application
Open your web browser and navigate to the presented link. The Chatbot application will be displayed, prompting you to input your OpenAI API Key. Engage in conversations by posing RTDIP-oriented questions and explore the capabilities of the application.

<div style="text-align:center">
  <img src="https://github.com/amosproj/amos2023ws05-pipeline-config-chat-ai/raw/feature-branch/UI.png" alt="UI" width="350"/>
</div>




