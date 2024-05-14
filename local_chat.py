import ollama  
import streamlit as st

# Import necessary Streamlit components
from streamlit import chat_input, chat_message, markdown, selectbox, session_state, title, write_stream

title("Personal GPT")

# Initialize history and model
session_state.setdefault("message", [])
session_state.setdefault("model", "")

# Initialize Models
if not session_state["model"]:
    models = [model["name"] for model in ollama.list()["models"]]
    session_state["model"] = selectbox("Choose Model", models)

# Model Generator
def model_res_gen():
    stream = ollama.chat(
        model=session_state["model"],
        messages=session_state["message"],
        stream=True
    )
    for chunk in stream:
        yield chunk["message"]["content"]

# Function to display chat messages
def display_chat_messages():
    for message in session_state["message"]:
        with chat_message(message["role"]):
            markdown(message["content"])

display_chat_messages()

# Handle new chat input
def handle_chat_input():
    if prompt := chat_input("What Up?"):
        # Add user message to history
        session_state["message"].append({"role": "user", "content": prompt})

        with chat_message("user"):
            markdown(prompt)

        with chat_message("assistant"):
            message = write_stream(model_res_gen())
            session_state["message"].append({"role": "assistant", "content": message})

handle_chat_input()

# Function to save current chat
def save_chat():
    if "archived_chats" not in session_state:
        session_state["archived_chats"] = []
    session_state["archived_chats"].append(session_state["message"])
    st.success("Chat saved!")

# Function to start a new chat
def start_new_chat():
    session_state["message"] = []
    st.success("Started new chat.")

# Add buttons for saving and starting a new chat
if st.button("Save Chat"):
    save_chat()
if st.button("New Chat"):
    start_new_chat()

# Function to display archived chats in the sidebar
def display_archived_chats():
    with st.sidebar:
        st.header("Chat History")
        if "archived_chats" in session_state:
            for i, chat in enumerate(session_state["archived_chats"]):
                with st.expander(f"Chat {i + 1}"):
                    for message in chat:
                        with chat_message(message["role"]):
                            markdown(message["content"])

display_archived_chats()
