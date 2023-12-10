
# app
import streamlit as st
import replicate
import os
import time

# App title
if 'page_config_set' not in st.session_state:
    st.set_page_config(page_title="RTDIP Pipeline Chatbot")
    st.session_state['page_config_set'] = True
# Use HTML/CSS to position the title at the top left
st.markdown(
    '''
    <style>
        .title {
            margin-top: -70px;
            margin-left: -180px;
        }
    </style>
    <div class="title"><h2>RTDIP Pipeline Chatbot</h2></div>
    ''',unsafe_allow_html=True)   
#st.title('RTDIP Pipeline Chatbot')
# Git repository link (replace with your repository URL)
git_repo_link = "[![Git Repository](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/rtdip/core/tree/develop)"
st.markdown(git_repo_link, unsafe_allow_html=True)


# Replicate Credentials
api_key_container = st.empty()
openai_api_key = api_key_container.text_input('Enter OpenAI API Key:', type='password')

# Check if OpenAI API Key is entered
if openai_api_key:
        # Store the API key in the session state 
        st.session_state['OPENAI_API_KEY'] = openai_api_key
        os.environ['OPENAI_API_KEY'] = openai_api_key
        success_message = st.success('API Key stored!')
        # Hide success message, input field, and chat messages after 3 seconds
        time.sleep(0)
        success_message.empty()
        api_key_container.empty()
else:
        st.warning('Invalid OpenAI API Key. Please enter a valid key.')
        
# Store LLM generated responses
if "conversations" not in st.session_state.keys():
    st.session_state.conversations = [{"title": "Default Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]}]

# Display or clear chat messages
for conversation in st.session_state.conversations:
    for message in conversation["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def clear_chat_history():
    st.session_state.conversations = [{"title": "Default Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]}]
#st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


# User-provided prompt
if 'OPENAI_API_KEY' in st.session_state and st.session_state['OPENAI_API_KEY']:
    from LLMModel import RAG as RAG
    if prompt := st.chat_input():
    # Get the conversation context
        conversation = st.session_state.conversations[-1]
    
    # Use the entire conversation context as input
        #context = "\n".join([message["content"] for message in conversation["messages"]])
    
    # Add the user's input to the conversation
        conversation["messages"].append({"role": "user", "content": prompt})

    # Display user's input in the chat
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response considering the entire conversation context
        with st.chat_message("assistant"):
            start_time = time.time()  # to calculate the time taken to generate the response
            with st.spinner("Generating..."):
                response = RAG.run(prompt)
                end_time = time.time()  # to calculate the time taken to generate the response
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)

    # Calculate the time taken
        response_time = end_time - start_time
        st.write(f"Response generated in {response_time:.2f} seconds.")

    # Add the assistant's response to the conversation
        message = {"role": "assistant", "content": full_response}
        conversation["messages"].append(message)
    
    

