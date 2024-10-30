import os
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama

# Initialize the Ollama model for use with agents
ollama_model = Ollama(model="openhermes")

# Optionally, set up OpenAI API key if using OpenAI models instead of Ollama
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Define your agents with specified roles and goals
researcher = Agent(
    role='Researcher',
    goal='Discover new insights',
    backstory="You're a world-class researcher working at a major data science company",
    verbose=True,
    allow_delegation=False,
    llm=ollama_model  # Using Ollama model
)

writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory="You're a renowned technical writer specializing in data-related content",
    verbose=True,
    allow_delegation=False,
    llm=ollama_model  # Using Ollama model
)

# Define tasks assigned to each agent
task1 = Task(description='Investigate the latest AI trends', agent=researcher)
task2 = Task(description='Write a blog post on AI advancements', agent=writer)

# Create a crew to manage agents and tasks in a sequential process
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    llm=ollama_model,  # Using Ollama model
    verbose=2,  # Set verbosity level for more detailed logging
    process=Process.sequential  # Set process to sequential execution
)

# Launch the crew to start the tasks
result = crew.kickoff()

# Print the final result for review
print("Crew task result:", result)

