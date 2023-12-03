from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory


load_dotenv("/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/ChatUI_streamlit/.env")
openai_api_key = os.getenv('OPENAI_API_KEY')

# check if the API key is loaded
assert openai_api_key is not None, "Failed to load the OpenAI API key from .env file. Please create .env file and add OPENAI_API_KEY = 'your key'"




llm = ChatOpenAI(model_name='gpt-3.5-turbo',openai_api_key=openai_api_key) # Load the LLM model
set_llm_cache(InMemoryCache())


embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key) # Load the embeddings

# This is the root directory for the documents i want to create the RAG from
repo_path = '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/RAG/pipelines'
loader = GenericLoader.from_filesystem(
    repo_path,
    glob="**/*",
    suffixes=[".py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
)
documents = loader.load()




python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
)
texts = python_splitter.split_documents(documents)


db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))
retriever = db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
)

memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True)





RAG = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

# question = "I would like to use RTDIP components to read from an eventhub using ‘connection string’ as the connection string, and ‘consumer group’ as the consumer group, transform using binary to string, and edge x transformer then write to delta, return only the python code "
#
# result = RAG(question)
# result["answer"]
# print(result["answer"])