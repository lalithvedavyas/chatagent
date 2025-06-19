import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import TextLoader
import chromadb

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI Embeddings and Chroma client
embeddings = OpenAIEmbeddings()

# Path to your folder containing .txt files (update this path accordingly)
documents_path = "/workspaces/chatagent/pmchatagent/data/.txt"  # Make sure to update the correct path

# Initialize Chroma client
client = chromadb.Client()

# Create or retrieve Chroma collection
collection = client.get_or_create_collection(name="project_management")

# Step 1: Load text documents from folder
def load_documents_from_folder(folder_path):
    """
    Load all .txt files from a specified folder and return them as documents.
    """
    documents = []
    
    # Loop through all files in the folder and load only .txt files
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            loader = TextLoader(file_path)
            documents.extend(loader.load())  # Add each document loaded
    return documents

# Step 2: Load documents from the specified folder
your_documents = load_documents_from_folder(documents_path)

# Step 3: Add documents to the Chroma collection
# Store each document in the Chroma collection (vector store)
for doc in your_documents:
    collection.add_document(doc)

# Step 4: Create a retrieval chain using ChatOpenAI
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(temperature=0), retriever=collection.as_retriever()
)

# Function to query the chain
def query_chain(query):
    return qa_chain.run(query)

