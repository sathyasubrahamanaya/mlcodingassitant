import streamlit as st
from crewai import Task, Crew

def display_chat(messages):
    """Display user and assistant messages in the chat interface."""
    for msg in messages:
        st.chat_message(msg["role"]).write(msg["content"])

def process_user_input(user_input, dataframe, agents, messages):
    """Process user input and generate assistant response by analyzing data and context."""
    # Configure the task using the appropriate agent
    task_description = (
        f"User query: {user_input}. DataFrame:\n{dataframe.head().to_string()}"
        if dataframe is not None
        else f"User query: {user_input}"
    )
    
    task = Task(
        description=task_description,
        agent=agents["Data_Assessment_Agent"],
        expected_output="Chat response"
    )
    
    # Execute the task
    crew = Crew(agents=list(agents.values()), tasks=[task], verbose=1)
    crew.kickoff()  # Execute the crew
    
    # Access the task's output directly
    response = task.output.raw  # Use task.output.raw for raw response
    
    # Append the assistant's response to the chat history
    messages.append({"role": "assistant", "content": response})