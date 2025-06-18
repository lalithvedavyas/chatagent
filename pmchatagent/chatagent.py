from dotenv import load_dotenv
load_dotenv() # This loads the .env file
# chatagent.py


import os
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from chromadb import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to load vectorstore (Chroma)
def load_vectorstore():
    """Load Chroma vectorstore"""
    embeddings = OpenAIEmbeddings()

    # Connect to Chroma client (assuming ChromaDB is used for embeddings storage)
    chroma_client = Client()
    vectorstore = chroma_client.get_or_create_collection(name="project_management_data")

    # You may need to adjust this depending on your actual database setup
    vectorstore.add_documents(documents=your_documents, embeddings=embeddings)

    return vectorstore

# Function to create the QA chain
def get_qa_chain(vectorstore):
    """Returns a QA chain with ChromaDB as the retriever"""
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    chat_model = ChatOpenAI(temperature=0, openai_api_key=openai.api_key)

    qa_chain = ConversationalRetrievalChain.from_llm(chat_model, retriever)

    return qa_chain
