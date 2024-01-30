import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language, RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma as ChromaCommunity, FAISS
from langchain.memory import ConversationSummaryMemory, ConversationBufferMemory
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from pathlib import Path

def get_script_directory():
    # Get the absolute path of the directory containing this script
    return os.path.dirname(os.path.abspath(__file__))

def initialize_components(openai_api_key):
    env_files_dir = Path(__file__).parent / 'openai_keys'

    # Ensure the directory exists
    if not env_files_dir.exists():
        raise FileNotFoundError("The 'openai_keys' directory does not exist.")

    # Iterate through each .env file in the directory
    for env_file in env_files_dir.glob('*.env'):
        # Load the .env file
        load_dotenv(env_file)

        # Retrieve the API key from the loaded .env file
        loaded_api_key = os.getenv("OPENAI_API_KEY")

        # Check if the loaded API key matches the provided key value
        if loaded_api_key == openai_api_key:
            assert openai_api_key is not None, "OpenAI API key is not provided"

    # Initialize the language model
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)

    # Load the embeddings
    embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key)

    # Load and split documents using GenericLoader and RecursiveCharacterTextSplitter
    root_dir = os.path.join(get_script_directory(), '..', 'RAG')
    loader = GenericLoader.from_filesystem(
        root_dir,
        glob="**/*",
        suffixes=[".py"],
        exclude=["**/non-utf8-encoding.py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=500)
    )
    documents = loader.load()
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
    )
    texts = python_splitter.split_documents(documents)

    # Create the FAISS and Chroma vector stores
    docsearch = FAISS.from_documents(texts, embeddings)
    db = ChromaCommunity.from_documents(texts, embeddings)
    retriver1 = docsearch.as_retriever()
    retriver2 = db.as_retriever(search_type="mmr", search_kwargs={"k": 8})

    # Initialize ConversationSummaryMemory
    conversation_memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True)

    # Initialize RetrievalQA with ConversationalRetrievalChain
    RAG = ConversationalRetrievalChain.from_llm(llm, retriever=retriver2, memory=conversation_memory)

    # Define tools and Initialize Agent with conversation memory
    tools = [
        Tool(
            name="RTDIP SDK",
            func=RAG.run,
            description="useful for when you need to answer questions about RTDIP",
        )
    ]
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=conversation_memory, handle_parsing_errors=True
    )

    # Set the LLM cache
    set_llm_cache(InMemoryCache())
    # Set the LLM cache
    set_llm_cache(InMemoryCache())

    return agent, RAG

    return agent, RAG

# Function to update and retrieve conversation context
def update_and_get_context(user_input, conversation_memory):
    conversation_memory.add_user_input(user_input)
    context = conversation_memory.get_conversation()
    model_input = "\n".join(context + [user_input])
    return model_input

