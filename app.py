# app.py

import streamlit as st
import cohere
from PIL import Image

# Set your Cohere API key here
co = cohere.Client('jiOXVoCCtYZHImJ8tTpTYhNfX8zCnlqhpAVVWGkW')

# Set page configuration
img = Image.open('E:\github\Cohere-LLM-Chatbot\static\images\logo.png')
st.set_page_config(page_title='Cohere-LLM-Chatbot', page_icon=img)

# HTML styling
st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container {{
            max-width: 100%;
            padding-top: 0rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 2rem;
        }}
        .reportview-container .main {{
            padding: 0rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.markdown("Welcome!!!")
    # Load image from local directory
    sidebar_image = Image.open('E:/github/Cohere-LLM-Chatbot/static//images/logo.png')
    st.image(sidebar_image, width=150 , use_column_width=True)
    user_name = st.text_input("Tenancy_name", "atossyntelcloud")
    language = st.selectbox("Roles", ["Developer", "Architect", "Management People,Functional,Others"])

# User Input and Messages
user_input = st.text_input("Say something")

def generate_response(input_text):
    response = co.generate(
        model='command',
        prompt=input_text,
        max_tokens=500,
        temperature=0.7,
        k=50,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
