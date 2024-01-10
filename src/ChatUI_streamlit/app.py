import streamlit as st
import os
import time
import requests
import openai
import subprocess
from datetime import datetime


class InvalidAPIKeyException(Exception):
    pass

# Function to check API key validity
def is_valid_api_key(key):
    url = "https://api.openai.com/v1/models/gpt-3.5-turbo-instruct"
    headers = {"Authorization": f"Bearer {key}"}
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def run_update_script():
    script_path = '../UpdateRAG/updateRAG.py'
    absolute_script_path = os.path.join(os.getcwd(), script_path)
    command = f'python "{absolute_script_path}"'
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        st.success("Successfully updated RAG.")
        return result.stdout
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to update RAG. Error: {e.stderr}")
        return e.stderr


    
    
def get_last_modified_time(folder_path):
    latest_mod_time = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_mod_time = os.path.getmtime(file_path)
                latest_mod_time = max(latest_mod_time, file_mod_time)
            except Exception as e:
                pass
    return datetime.fromtimestamp(latest_mod_time).strftime("%Y-%m-%d %H:%M") if latest_mod_time else None

# Initialize page configuration once
if 'page_config_set' not in st.session_state:
    st.set_page_config(page_title="RTDIP Pipeline Chatbot")
    st.session_state['page_config_set'] = True

# HTML/CSS for title and GitHub link
st.markdown(
    '''
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="margin-top: -70px; margin-left: -180px;"><h2>RTDIP Pipeline Chatbot</h2></div>
        <div style="margin-top: -70px; "><a href="https://github.com/rtdip/core/tree/develop"><img src="https://img.shields.io/badge/GitHub-Repo-blue?logo=github"></a></div>
    </div>
    ''', unsafe_allow_html=True)


rag_folder_path = os.path.join("..", "RAG")

last_modified_time = get_last_modified_time(rag_folder_path)

left_col, right_col = st.columns([3, 1])  

with right_col:
    if st.button('Update RAG'):
        run_update_script()
    st.caption(f"Last update: {last_modified_time}")  

with left_col:
    st.write("")  # This will create space and push the button and text to the right

# Check if the OpenAI API key is already stored in the session
if 'OPENAI_API_KEY' not in st.session_state:
    # If not, ask the user to input it
    openai_api_key = st.text_input('Enter OpenAI API Key:', type='password')
    if openai_api_key:
        try:
            if is_valid_api_key(openai_api_key):
                st.session_state['OPENAI_API_KEY'] = openai_api_key
                os.environ['OPENAI_API_KEY'] = openai_api_key
                st.success('API Key stored!')
            else:
                raise InvalidAPIKeyException
        except InvalidAPIKeyException:
            st.error('Invalid OpenAI API Key. Please enter a valid key.')

# Store LLM generated responses
if "conversations" not in st.session_state.keys():
    st.session_state.conversations = [{"title": "Default Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]}]

# Display or clear chat messages
for conversation in st.session_state.conversations:
    for message in conversation["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# User-provided prompt
if 'OPENAI_API_KEY' in st.session_state and st.session_state['OPENAI_API_KEY']:
    from LLMModel import RAG as RAG
    if prompt := st.chat_input():
        conversation = st.session_state.conversations[-1]
        context = "\n".join([message["content"] for message in conversation["messages"]])
        conversation["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            start_time = time.time()
            with st.spinner("Generating..."):
                response = RAG.run(context + "\n" + prompt)
                end_time = time.time()
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        response_time = end_time - start_time
        st.write(f"Response generated in {response_time:.2f} seconds.")
        message = {"role": "assistant", "content": full_response}
        conversation["messages"].append(message)
