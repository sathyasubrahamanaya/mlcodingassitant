from crewai import Agent
from langchain_groq import ChatGroq

def create_agents(llm):
    return {
        "Problem_Definition_Agent": Agent(
            role="Problem Definition Agent",
            goal="Clarify ML problem type & requirements",
            backstory="This agent specializes in understanding and defining machine learning problems based on user input.",
            llm=llm,
            verbose=False,
            allow_delegation=False
        ),
        "Data_Assessment_Agent": Agent(
            role="Data Assessment Agent",
            goal="Evaluate data quality and preprocessing needs",
            backstory="This agent assesses the data's suitability and recommends preprocessing steps for better model performance.",
            llm=llm,
            verbose=False,
            allow_delegation=False
        ),
        "Model_Recommendation_Agent": Agent(
            role="Model Recommendation Agent",
            goal="Suggest suitable ML models with rationale",
            backstory="This agent recommends the most appropriate machine learning models based on the problem definition and data assessment.",
            llm=llm,
            verbose=False,
            allow_delegation=False
        ),
        "Benchmarking_Agent": Agent(
            role="Benchmarking Agent",
            goal="Simulate model performance and generate reports",
            backstory="This agent evaluates model performance and provides a comparative analysis of different models.",
            llm=llm,
            verbose=False,
            allow_delegation=False
        ),
        "Code_Generation_Agent": Agent(
            role="Code Generation Agent",
            goal="Generate starter code for the project",
            backstory="This agent creates project-ready code templates to kickstart development.",
            llm=llm,
            verbose=False,
            allow_delegation=False
        )
    }