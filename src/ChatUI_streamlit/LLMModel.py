import os
from langchain.retrievers import BM25Retriever
from langchain.chains import RetrievalQA
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.document_loaders.text import TextLoader
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma as Chroma
from langchain.vectorstores import LanceDB
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.retrievers.merger_retriever import MergerRetriever
from langchain_community.document_transformers import (EmbeddingsClusteringFilter,EmbeddingsRedundantFilter,)
from langchain.retrievers.document_compressors import DocumentCompressorPipeline
from langchain.retrievers import ContextualCompressionRetriever
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import Language
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
import lancedb
from langchain.embeddings.fake import FakeEmbeddings
from langchain.docstore import InMemoryDocstore
from langchain.docstore.document import Document
import faiss


# Load the OpenAI API key
load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]
assert openai_api_key is not None, "Failed to load the OpenAI API key from .env file. Please create .env file and add OPENAI_API_KEY = 'your key'"

# Initialize the language model
llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)

# Load the embeddings
embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key)


###############  first content store using FAISS
# # Load and split documents
#root_dir = '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG/pipelines'
root_dir = 'C://Users//lynda//OneDrive//Bureau//pc//amos2023ws05-pipeline-config-chat-ai//src//RAG'
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
     for file in filenames:
         try:
           loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
           docs.extend(loader.load_and_split())
         except Exception as e:
            pass  # Consider logging the exception for debugging

# # Create the FAISS index
docsearch = FAISS.from_documents(docs, embeddings)
# save the vector store offline for later use
#faiss.write_index(docsearch.index, '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/ChatUI_streamlit/faiss_index_file')
docsearch.save_local("C://Users//lynda//OneDrive//Bureau//pc//amos2023ws05-pipeline-config-chat-ai//src//ChatUI_streamlit//faiss_index")
docsearch = FAISS.load_local("faiss_index", embeddings)
retriever1= docsearch.as_retriever()
# Check if the FAISS index is loaded properly
if docsearch.index.ntotal > 0:
    print("FAISS index is loaded and contains documents.")
else:
    print("FAISS index is loaded but contains no documents.")

############### second content store using LANCEDB

loader = GenericLoader.from_filesystem(
    "C://Users//lynda//OneDrive//Bureau//pc//amos2023ws05-pipeline-config-chat-ai//src//RAG",
    glob="**/*",
    suffixes=[".py"],
    exclude=["**/non-utf8-encoding.py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
)
documents = loader.load()

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
)
texts = python_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key)

db = lancedb.connect("/tmp/lancedb")
table = db.create_table(
    "my_table",
    data=[
        {
            "vector": embeddings.embed_query("Rtdip"),
            "text": "Rtdip",
            "id": "1",
        }
    ],
    mode="overwrite",
)


lance_db = LanceDB.from_documents(texts, embeddings, connection=table)
# Create a LanceDB retriever
retriever2 = lance_db.as_retriever()

# Check if the LanceDB table has documents
print(dir(lance_db))




# Check if _get_relevant_documents is implemented in retriever 1 and 2
if hasattr(retriever1, '_get_relevant_documents'):
    print("retriever1 has _get_relevant_documents method.")
else:
    print("retriever1 does not have _get_relevant_documents method.")
if hasattr(retriever2, '_get_relevant_documents'):
    print("retriever2 has _get_relevant_documents method.")
else:
    print("retriever2 does not have _get_relevant_documents method.")
    

    
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)

lotr = MergerRetriever(retrievers=[retriever1, retriever2])
RAG = ConversationalRetrievalChain.from_llm(llm, retriever=lotr, memory=memory)


# Set the LLM cache
set_llm_cache(InMemoryCache())

# Function to update and retrieve conversation context
def update_and_get_context(user_input, conversation_memory):
    conversation_memory.add_user_input(user_input)
    context = conversation_memory.get_conversation()
    model_input = "\n".join(context + [user_input])
    return model_input


test_query = " I would like to use RTDIP components to read from PythonDeltaSharingSource, transform using SSIPPIBinaryFileToPCDMTransformer, then write to SparkEventhubDestination"

# Test FAISS retriever
faiss_results = retriever1.get_relevant_documents(test_query)
print("FAISS results:", faiss_results)


# Test LanceDB retriever
lance_results = retriever2.get_relevant_documents(test_query)
print("LanceDB results:", lance_results)
