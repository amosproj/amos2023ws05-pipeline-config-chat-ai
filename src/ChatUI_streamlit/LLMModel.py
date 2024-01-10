#%%
import os
from langchain.chains import RetrievalQA
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.vectorstores import FAISS
from langchain.document_loaders.text import TextLoader
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
# import faiss
from langchain.vectorstores import FAISS as FAISS
import faiss 

# Load the OpenAI API key

openai_api_key = os.environ["OPENAI_API_KEY"]
assert openai_api_key is not None, "Failed to load the OpenAI API key from .env file. Please create .env file and add OPENAI_API_KEY = 'your key'"

# Initialize the language model
llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)

# Load the embeddings
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key)

# # Load and split documents
# root_dir = '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG/pipelines'
# docs = []
# for dirpath, dirnames, filenames in os.walk(root_dir):
#     for file in filenames:
#         try:
#             loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
#             docs.extend(loader.load_and_split())
#         except Exception as e:
#             pass  # Consider logging the exception for debugging

# # Create the FAISS index
# docsearch = FAISS.from_documents(docs, embeddings)

#%%
# save the vector store offline for later use
# faiss.write_index(docsearch.index, '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/ChatUI_streamlit/faiss_index_file')
# docsearch.save_local("/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/ChatUI_streamlit/faiss_index")

#%%
docsearch = FAISS.load_local("faiss_index", embeddings)
#%%
# Initialize RetrievalQA
RAG = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=docsearch.as_retriever())

# Define tools
tools = [
    Tool(
        name="RTDIP SDK",
        func=RAG.run,
        description="useful for when you need to answer questions about RTDIP",
    )
]

# Initialize conversation memory
conversation_memory = ConversationBufferMemory()

# Initialize Agent with conversation memory
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=conversation_memory, handle_parsing_errors=True
)

# Set the LLM cache
set_llm_cache(InMemoryCache())

# Function to update and retrieve conversation context
def update_and_get_context(user_input, conversation_memory):
    conversation_memory.add_user_input(user_input)
    context = conversation_memory.get_conversation()
    model_input = "\n".join(context + [user_input])
    return model_input

# Example usage (commented out for testing)
# user_input = "What's the weather like today?"
# model_input = update_and_get_context(user_input, conversation_memory)
# response = llm.run(model_input)
# print(response)

# Note: You can uncomment and modify the testing code as per your use case.

# %%
