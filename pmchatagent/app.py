
import streamlit as st
from chatbot import get_qa_chain, load_vectorstore
import os

# Set up Streamlit interface
st.set_page_config(page_title="Project Management Chatbot", layout="wide")

# Load vectorstore and QA chain
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = get_qa_chain()

# Set up page title and description
st.markdown("This chatbot uses project management methodology to answer your questions.")

# Ask user for their query
user_input = st.text_input("Ask a question about Project Management:", "")

# Check if there is any input and process the query
if user_input:
    response = st.session_state.qa_chain.run(user_input)
    st.write("Answer:", response)
else:
    st.write("Please ask a question.")

