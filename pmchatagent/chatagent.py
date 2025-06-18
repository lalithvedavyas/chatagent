
from dotenv import load_dotenv
load_dotenv()

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os

def load_vectorstore(directory="data"):
    texts = []
    for fname in os.listdir(directory):
        if fname.endswith(".txt"):
            with open(os.path.join(directory, fname), "r", encoding="utf-8") as f:
                texts.append(f.read())

    documents = [Document(page_content=text) for text in texts]
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(documents, embeddings, persist_directory="chroma_db")
    db.persist()
    return db

def get_qa_chain():
    db = Chroma(persist_directory="chroma_db", embedding_function=OpenAIEmbeddings())
    retriever = db.as_retriever()
    llm = ChatOpenAI(temperature=0.2)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain

