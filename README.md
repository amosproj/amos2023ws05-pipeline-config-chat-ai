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
Software Developerss: [@lyndanajjar](https://github.com/lyndanajjar), [@bergzain](https://github.com/bergzain), [@Obismadi99](https://github.com/Obismadi99), [@Nahrain1](https://github.com/Nahrain1)

The planning document of the team is found [here](https://docs.google.com/spreadsheets/d/1m1z2m_p6k0ATw0RVNXJMbDp-RrOOPxpu0c3PPCtrwBI/edit#gid=6) 

## Prerequisites
Ensure that you have installed:

* Python version 3.11 or higher
* Docker Desktop 
* OpenAI API Key   

## Build Process 
Clone the github repository: 
```
git clone https://github.com/amosproj/amos2023ws05-pipeline-config-chat-ai.git
``` 

To install the required dependencies for this project, please create a virtual environment and run: 
```
pip install -r requirements.txt
```

The application is run using the docker application, so ensure the Docker daemon is running. First, build the image using the command: 

```
docker build -t <your-image-name> .
```

In a second step, type the run command to create the container. Note that we are using port 8501, as it is the default port used by Streamlit: 

```
docker run -dp 8501:8501 <your-image-name>
```

After successfully running the container, you can access the application by clicking on the link displayed in the `Ports` column within the Docker Desktop interface. This link corresponds to the port mapping configured during the container's launch and serves as the entry point to interact with the application. 

_Note_: Don't forget to replace `<your-image-name>` with the actual name you chose for your Docker image.

The Chatbot application is then presented within your browser window, prompting you to input your OpenAI API Key and engage in conversations by posing RTDIP-oriented questions. 





