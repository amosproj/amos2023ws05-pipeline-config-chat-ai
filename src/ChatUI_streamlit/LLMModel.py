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




llm = ChatOpenAI(model_name='gpt-3.5-turbo',openai_api_key=openai_api_key) # Load the LLM model
# set_llm_cache(InMemoryCache())


embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key) # Load the embeddings
#
# # This is the root directory for the documents i want to create the RAG from
# repo_path = '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG'
# loader = GenericLoader.from_filesystem(
#     repo_path,
#     glob="**/*",
#     suffixes=[".py"],
#     parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
# )
# documents = loader.load()
#
# python_splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
# )
# texts = python_splitter.split_documents(documents)
#
#
# db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))
# retriever = db.as_retriever(
#     search_type="mmr",  # Also test "similarity"
#     search_kwargs={"k": 8},
# )

##########################################  the old version of RAG
# This is the root directory for the documents i want to create the RAG from
root_dir = '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG/pipelines'
docs = [] # Create an empty list to store the docs

# Go through each folder to extract all the files
for dirpath, dirnames, filenames in os.walk(root_dir):

    # Go through each file
    for file in filenames:
        try:
            # Load up the file as a doc and split
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e:
            pass

docsearch = FAISS.from_documents(docs, embeddings) # Create the FAISS index
# source https://python.langchain.com/docs/integrations/vectorstores/faiss_async


#memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True)
# add caching to the memory


RAG = RetrievalQA.from_chain_type(llm,chain_type="stuff" ,retriever=docsearch.as_retriever()) # the old chain for the retrieval
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
