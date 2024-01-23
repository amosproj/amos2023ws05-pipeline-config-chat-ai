#%%
import os
from langchain.chains import RetrievalQA
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma as Chroma
from langchain.retrievers.merger_retriever import MergerRetriever
from langchain_community.document_transformers import (
    EmbeddingsClusteringFilter,
    EmbeddingsRedundantFilter,
)
from langchain.retrievers.document_compressors import DocumentCompressorPipeline
from langchain.retrievers import ContextualCompressionRetriever

from dotenv import load_dotenv

from langchain.chains import ConversationalRetrievalChain


from langchain.text_splitter import Language
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser

#%%
# Load the OpenAI API key
load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]
assert openai_api_key is not None, "Failed to load the OpenAI API key from .env file. Please create .env file and add OPENAI_API_KEY = 'your key'"

# Initialize the language model
llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)

# Load the embeddings
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key)


##### first content store using faiss
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
# docsearch = FAISS.load_local("/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/ChatUI_streamlit/faiss_index", embeddings)
# retriver1= docsearch.as_retriever()

#%%
# Initialize RetrievalQA


#%%
############### second content store using chroma

loader = GenericLoader.from_filesystem(
    "/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG",
    glob="**/*",
    suffixes=[".py"],
    exclude=["**/non-utf8-encoding.py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
)
documents = loader.load()
len(documents)
#%%

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
)
texts = python_splitter.split_documents(documents)
len(texts)

#%%
db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=(),openai_api_key=openai_api_key))
# this will save and load the vector store from local folder
# db = Chroma(persist_directory="/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/ChatUI_streamlit/chroma_index")

retriver2 = db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
)

#%%

memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)

RAG = ConversationalRetrievalChain.from_llm(llm, retriever=retriver2, memory=memory)


# RAG = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=retriver2)

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