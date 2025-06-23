import streamlit as st
from agents import create_agents
from chat import display_chat, process_user_input
from data_handler import load_dataframe
from tasks import setup_tasks
import json
import os

# File to store chat history
CHAT_HISTORY_FILE = "chat_history.json"

def load_chat_history():
    """Load chat history from a JSON file."""
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_chat_history(messages):
    """Save chat history to a JSON file."""
    with open(CHAT_HISTORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)

def main():
    st.set_page_config(layout="wide")
    st.title("ML Assistant Chat :speech_balloon:")

    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = load_chat_history()
    if 'dataframe' not in st.session_state:
        st.session_state.dataframe = None

    # Load Groq API key from secrets
    groq_api_key = "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"
    os.environ["GROQ_API_KEY"] = groq_api_key

    # Model Selection
    model = st.sidebar.selectbox(
        'Choose a model',
        ['groq/llama3-8b-8192', 'groq/mixtral-8x7b-32768', 'groq/gemma2-9b-it','groq/llama-3.3-70b-versatile']
    )

    # Initialize LLM
    from crewai import LLM
    llm = LLM(
        model=model,
        temperature=0.7
    )

    # Create agents
    agents = create_agents(llm)

    # File Upload
    uploaded_file = st.file_uploader("Upload CSV (.csv)", type=["csv"])
    if uploaded_file is not None:
        try:
            df = load_dataframe(uploaded_file)
            st.session_state.dataframe = df
        except Exception as e:
            st.error(f"Error loading CSV: {e}")

    # Display existing chat messages
    display_chat(st.session_state.messages)

    # User input and processing
    user_input = st.chat_input("Ask your ML question here")
    if user_input:
        # Add user message to chat history and save immediately
        user_msg = {"role": "user", "content": user_input}
        st.session_state.messages.append(user_msg)
        save_chat_history(st.session_state.messages)

        # Process user input and generate assistant response
        with st.spinner("Generating response..."):
            process_user_input(user_input, st.session_state.dataframe, agents, st.session_state.messages)
            save_chat_history(st.session_state.messages)

        # Force a rerun to display updated messages
        st.rerun()

    # Add a button to clear chat history
    if len(st.session_state.messages) > 0:
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            save_chat_history([])

if __name__ == "__main__":
    main()