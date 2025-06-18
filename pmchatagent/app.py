# app.py
import streamlit as st
from chatagent import get_qa_chain, load_vectorstore

# Set up the page configuration
st.set_page_config(page_title="Project Management Chatbot", layout="wide")

# Title of the web app
st.title("Project Management Chatbot")

# Instructions
st.write("""
    Welcome to the Project Management Chatbot! You can ask questions about project management methodologies.
    Try asking me anything like:
    - What is Agile?
    - How does Scrum work?
    - What are the advantages of using Kanban?
""")

# Add an input box for user query
user_query = st.text_input("Ask a question:")

# If the user submits a query
if user_query:
    # Load the vectorstore (this should load the project management data)
    vectorstore = load_vectorstore()

    # Get the QA chain for answering questions
    qa_chain = get_qa_chain(vectorstore)

    # Get the answer from the chain
    answer = qa_chain.run(user_query)

    # Display the answer
    st.write(answer)
