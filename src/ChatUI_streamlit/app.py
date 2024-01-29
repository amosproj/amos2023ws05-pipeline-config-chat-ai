import streamlit as st
import os
import time
import requests
import subprocess
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
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
# Function to load API keys from the openai_keys directory
def load_api_keys():
    # Get the directory of the current script file
    script_dir = Path(__file__).parent

    # Path to the 'openai_keys' directory
    keys_dir = script_dir / 'openai_keys'

    # Create the directory if it doesn't exist
    keys_dir.mkdir(exist_ok=True)

    # Dictionary to store the API keys
    api_keys = {}

    # Iterate through each .env file in the directory
    for env_file in keys_dir.glob('*.env'):
        # Load the .env file
        load_dotenv(env_file)

        # Extract the key name and API key
        key_name = env_file.stem
        api_key = os.getenv('OPENAI_API_KEY')

        # Add the key to the dictionary if it's valid
        if api_key:
            api_keys[key_name] = api_key

    return api_keys

def initialize_chat_components():
    api_key = st.session_state.get('OPENAI_API_KEY')
    assert api_key is not None, "OpenAI API key is not provided"

    if 'components_initialized' not in st.session_state:
        from LLMModel import initialize_components
        st.session_state.agent, st.session_state.RAG = initialize_components(api_key)
        st.session_state['components_initialized'] = True# Function to add or select an API key

def api_key_selection(api_keys):
    # Path to the directory where the script is located
    script_directory = Path(__file__).parent

    # Path to the 'openai_keys' folder at the same level as the script
    openai_keys_dir = script_directory / 'openai_keys'

    selected_key_name = st.sidebar.selectbox('Select an API Key', options=list(api_keys.keys()), index=0)
    if selected_key_name and api_keys[selected_key_name] != st.session_state.get('OPENAI_API_KEY', None):
        st.session_state['OPENAI_API_KEY'] = api_keys[selected_key_name]
        if is_valid_api_key(api_keys[selected_key_name]):
            st.sidebar.success(f'Selected API Key: {selected_key_name}')
        else:
            st.sidebar.error('Invalid API Key. Please select a valid key.')
            if 'OPENAI_API_KEY' in st.session_state:
                del st.session_state['OPENAI_API_KEY']
    
    new_key_name = st.sidebar.text_input('Name for new API Key:')
    new_key_value = st.sidebar.text_input('Enter new OpenAI API Key:', type='password')
    if st.sidebar.button('Save API Key'):
        try:
            if new_key_name and new_key_value and is_valid_api_key(new_key_value):
                # Create the 'openai_keys' directory if it doesn't exist
                openai_keys_dir.mkdir(parents=True, exist_ok=True)

                # Path to the new API key file
                new_env_file = openai_keys_dir / f'{new_key_name}.env'

                # Write the API key to the file
                with new_env_file.open('w') as file:
                    file.write(f'OPENAI_API_KEY={new_key_value}\n')

                api_keys[new_key_name] = new_key_value
                st.session_state['OPENAI_API_KEY'] = new_key_value
                initialize_chat_components()
                st.sidebar.success(f'New API Key "{new_key_name}" saved and activated')
            else:
                st.sidebar.error('Invalid or missing data for new API Key.')
        except Exception as e:
            st.sidebar.error(f'An error occurred: {e}')

# Function to check API key and update if necessary
def check_and_update_api_key():
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
def run_update_script():
    root_directory = Path(__file__).parents[1]  # This navigates two levels up from the current file
    update_script_path = root_directory / 'UpdateRAG' / 'updateRAG.py'  # Specify the script name if it's a file

    # Convert to absolute path
    absolute_script_path = update_script_path.resolve()


    # Construct the command
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
    return datetime.fromtimestamp(latest_mod_time).strftime("%Y-%m-%d") if latest_mod_time else None
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
# Load API keys
api_keys = load_api_keys()
# Add API key selection UI
api_key_selection(api_keys)
# Check and update API key
check_and_update_api_key()
rag_folder_path = os.path.join("..", "RAG")
last_modified_time = get_last_modified_time(rag_folder_path)
left_col, right_col = st.columns([3, 1])
with right_col:
    button_style = """
    <style>
    .stButton>button {
       max-width: 200px;
    margin-left: 45px;
    padding: 5px 10px;
    border-radius: 15px;
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)
    if st.button('Update RAG'):
        run_update_script()
    st.caption(f"Last update: {last_modified_time}")
with left_col:
    st.write("")  # This will create space and push the button and text to the right
if 'conversations' not in st.session_state:
    st.session_state.conversations = [{"title": "Default Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]}]
# Check if the OpenAI API key is set in the session state
if 'OPENAI_API_KEY' in st.session_state and is_valid_api_key(st.session_state['OPENAI_API_KEY']):
    initialize_chat_components()
    # Initialize components with OpenAI API key
    # Display all messages in the current conversation
    conversation = st.session_state.conversations[-1]
    for message in conversation["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    if prompt := st.chat_input():
        context = "\n".join([message["content"] for message in conversation["messages"]])
        conversation["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            start_time = time.time()
            with st.spinner("Generating..."):
                response = st.session_state.RAG.run(prompt)
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
    if 'run_button' in st.session_state and st.session_state.run_button == True:
        st.session_state.running = True
    else:
        st.session_state.running = False
    if st.button("New Conversation", disabled=st.session_state.running, key='run_button'):
        # Start a new conversation
        st.session_state.conversations.append({"title": "New Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]})
        # Trigger a rerun
        st.rerun()
else:
    # If the API key is not set, continue showing the API key selection UI
    st.write("Please select or enter an OpenAI API key to continue.")





