from crewai import Task

def setup_tasks(agents, user_question, dataframe=None):
    problem_task = Task(
        description=user_question,
        agent=agents["Problem_Definition_Agent"],
        expected_output="Problem definition"
    )
    
    data_task = Task(
        description=f"Assess data: {dataframe.head()}" if dataframe is not None else "Assess hypothetical data",
        agent=agents["Data_Assessment_Agent"],
        expected_output="Data assessment or hypothetical report"
    )
    
    return problem_task, data_task