# Use Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /usr/app/src

# Set a default locale
ARG LANG='en_US.UTF-8'

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    apt-utils \
    build-essential \
    locales \
    python3-pip \
    python3-dev \
    rsyslog \
    systemd \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Generate the specified locale
RUN locale-gen ${LANG}

# Upgrade pip
RUN pip3 install --upgrade pip

# Copy the requirements.txt file into the container
COPY requirements.txt ./

# Install Python dependencies
RUN pip3 install -r requirements.txt
# Copy the RAG folder, .env file, and ChatUI_streamlit folder into the container
COPY RAG/ RAG/
#COPY ChatUI_streamlit/.streamlit .streamlit
COPY ChatUI_streamlit/LLMModel.py/ LLMModel.py

# Copy the app.py file
COPY ChatUI_streamlit/app.py ./

# Make the port 8501 available to the world outside this container
EXPOSE 8501:8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
