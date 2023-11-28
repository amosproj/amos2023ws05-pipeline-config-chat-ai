import streamlit as st
import replicate
import os
from LLMModel import RAG as RAG

# App title
st.set_page_config(page_title="RTDIP PipeLine Chatbot")

# Replicate Credentials
with st.sidebar:
    st.title('RTDIP Pipeline Generation Chatbot')
    # if 'REPLICATE_API_TOKEN' in st.secrets:
    #     st.success('API key already provided!', icon='✅')
    #     replicate_api = st.secrets['REPLICATE_API_TOKEN']
    # else:
    #     replicate_api = st.text_input('Enter Replicate API token:', type='password')
    #     if not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
    #         st.warning('Please enter your credentials!', icon='⚠️')
    #     else:
    #         st.success('Proceed to entering your prompt message!', icon='👉')
    # os.environ['REPLICATE_API_TOKEN'] = replicate_api
    openai_api_key = os.getenv('OPENAI_API_KEY', 'YourAPIKey')

# Store LLM generated responses
if "conversations" not in st.session_state.keys():
    st.session_state.conversations = [{"title": "Default Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]}]

# Chat history on the left
st.sidebar.subheader('Chat History')

# Button to load previous conversations
if st.sidebar.button('Load Previous Conversations'):
    st.sidebar.text('Select a conversation to open:')
    selected_conversation = st.sidebar.selectbox('', range(len(st.session_state.conversations)), format_func=lambda x: st.session_state.conversations[x]["title"])

    # Display the selected conversation
    conversation = st.session_state.conversations[selected_conversation]
    for message in conversation["messages"]:
        with st.expander(conversation["title"]):
            with st.chat_message(message["role"]):
                st.write(message["content"])

# Display or clear chat messages
for conversation in st.session_state.conversations:
    for message in conversation["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def clear_chat_history():
    st.session_state.conversations = [{"title": "Default Conversation", "messages": [{"role": "assistant", "content": "How may I assist you today?"}]}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


# User-provided prompt
if prompt := st.chat_input(): #
    # Use the user's prompt as the title 
    title = prompt
    
    st.session_state.conversations[-1]["title"] = title
    st.session_state.conversations[-1]["messages"].append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if the last message is not from the assistant
if st.session_state.conversations[-1]["messages"][-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Generating..."):
            response = RAG.run(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)

    message = {"role": "assistant", "content": full_response}
    st.session_state.conversations[-1]["messages"].append(message)
    
    
    
    
