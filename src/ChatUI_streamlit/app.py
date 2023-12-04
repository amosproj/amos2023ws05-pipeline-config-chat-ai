
# app
import streamlit as st
import replicate
import os
import time

# App title
if 'page_config_set' not in st.session_state:
    st.set_page_config(page_title="RTDIP PipeLine Chatbot")
    st.session_state['page_config_set'] = True

# Replicate Credentials
with st.sidebar:
    st.title('RTDIP Pipeline Generation Chatbot')
    openai_api_key = st.text_input('Enter OpenAI API Key:', type='password')

# Check if OpenAI API Key is entered
if openai_api_key:
    # Store the API key in the session state or environment variable
    st.session_state['OPENAI_API_KEY'] = openai_api_key
    os.environ['OPENAI_API_KEY'] = openai_api_key
    st.success('API Key stored!')
else:
    st.warning('Please enter your OpenAI API Key to proceed.')


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
if 'OPENAI_API_KEY' in st.session_state and st.session_state['OPENAI_API_KEY']:
    from LLMModel import RAG as RAG
    if prompt := st.chat_input():
    # Get the conversation context
        conversation = st.session_state.conversations[-1]
    
    # Use the entire conversation context as input
        context = "\n".join([message["content"] for message in conversation["messages"]])
    
    # Add the user's input to the conversation
        conversation["messages"].append({"role": "user", "content": prompt})

    # Display user's input in the chat
        with st.chat_message("user"):
            st.write(prompt)

        start_time = time.time() # to calculate the time taken to generate the response
    # Generate a new response considering the entire conversation context
        with st.chat_message("assistant"):
            with st.spinner("Generating..."):
                response = RAG.run(context)
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)

        end_time = time.time() # to calculate the time taken to generate the response
    # Calculate the time taken
        response_time = end_time - start_time
        st.write(f"Response generated in {response_time:.2f} seconds.")

    # Add the assistant's response to the conversation
        message = {"role": "assistant", "content": full_response}
        conversation["messages"].append(message)
    
    
