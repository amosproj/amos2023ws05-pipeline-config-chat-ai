import streamlit as st
import os
import time
import requests
from dotenv import load_dotenv
from pathlib import Path

class InvalidAPIKeyException(Exception):
    pass

# Function to load API keys from the openai_keys directory
def load_api_keys():
    keys_dir = Path('openai_keys')
    keys_dir.mkdir(exist_ok=True)
    api_keys = {}
    for env_file in keys_dir.glob('*.env'):
        load_dotenv(env_file)
        key_name = env_file.stem
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            api_keys[key_name] = api_key
    return api_keys

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

# Initialize page configuration once
if 'page_config_set' not in st.session_state:
    st.set_page_config(page_title="RTDIP Pipeline Chatbot")
    st.session_state['page_config_set'] = True

# HTML/CSS for title and GitHub link
st.markdown(
    '''
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h2 style="margin: 0;">RTDIP Pipeline Chatbot</h2>
        <a href="https://github.com/rtdip/core/tree/develop">
            <img src="https://img.shields.io/badge/GitHub-Repo-blue?logo=github" alt="GitHub Repo">
        </a>
    </div>
    ''', unsafe_allow_html=True)

# Function to add or select an API key
def api_key_selection(api_keys):
    selected_key_name = st.sidebar.selectbox('Select an API Key', options=list(api_keys.keys()), index=0)
    if selected_key_name:
        st.session_state['OPENAI_API_KEY'] = api_keys[selected_key_name]
        st.sidebar.success(f'Selected API Key: {selected_key_name}')
    new_key_name = st.sidebar.text_input('Name for new API Key:')
    new_key_value = st.sidebar.text_input('Enter new OpenAI API Key:', type='password')
    if st.sidebar.button('Save API Key'):
        if new_key_name and new_key_value and is_valid_api_key(new_key_value):
            new_env_file = Path(f'openai_keys/{new_key_name}.env')
            with new_env_file.open('w') as file:
                file.write(f'OPENAI_API_KEY={new_key_value}\n')
            st.sidebar.success(f'New API Key "{new_key_name}" saved')
        else:
            st.sidebar.error('Invalid or missing data for new API Key.')

api_keys = load_api_keys()
api_key_selection(api_keys)

if "conversations" not in st.session_state.keys():
    st.session_state.conversations = [{"title": "Default Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]}]

# Check if the API key is set in the session state
if 'OPENAI_API_KEY' in st.session_state and st.session_state['OPENAI_API_KEY']:
    from LLMModel import initialize_components, update_and_get_context
    
    agent, RAG = initialize_components(st.session_state['OPENAI_API_KEY'])


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
else:
    # If the API key is not set, continue showing the API key selection UI
    st.write("Please select or enter an OpenAI API key to continue.")
