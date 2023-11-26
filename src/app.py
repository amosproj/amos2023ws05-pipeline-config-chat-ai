import streamlit as st
import requests

st.title("Simple Chat with GPT-2")

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/rwl4/gpt2-medium-chat"
headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_TOKEN"}

# Function to query the Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Initialize session state for model and messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if 'input_key' not in st.session_state:
    st.session_state['input_key'] = 0

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
user_input = st.text_input("Your message:", key=f'input_{st.session_state.input_key}')

if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state["messages"].append({"role": "user", "content": user_input})

        try:
            # Fetch response from Hugging Face API
            output = query({
                "inputs": user_input
            })

            # Handle the response
            if isinstance(output, list) and output:
                assistant_response = output[0]['generated_text']
            else:
                assistant_response = "No response or unexpected response format."

            # Append the assistant response to chat history
            st.session_state["messages"].append({"role": "assistant", "content": assistant_response})

        except Exception as e:
            st.error(f"An error occurred: {e}")

        # Increment the key to clear the input box
        st.session_state.input_key += 1

        # Rerun the app to update the chat display
        st.experimental_rerun()
