from langchain_community.llms import Ollama
from crewai import Crew, Task, Agent
from langchain_community.tools import DuckDuckGoSearchRun

model=Ollama(model="deepseek-r1")
search_tool=DuckDuckGoSearchRun()
analyer=Agent(
    role="Input Analyzer",
    goal="Extract topic,level and goal from the input",
    backstory="You are a precise parser of educational requests, breaking tthem clear components",
    llm=model,
    verbose=True
)
searcher=Agent(
    role="Research Assistant",
    goal="Find the best resources for the topic and level",
    backstory="You are a research assistant, finding the best open source resources for the topic and levelin order to help the user achieve their goal",
    tools=[search_tool],
    llm=model,
    verbose=True
)
project=Agent(
    role="Project Idea Generator",
    goal="Generate project ideas based on the topic and level to reinforce the learning",
    backstory="You are a mentor that provides creative hands on projects to reinforce the learning",
    llm=model,
    verbose=True
)
designer=Agent(
    role="Curriculum Bulider",
    goal="Create a structured learning path with a clear timeline which includes the resources and projects",
    backstory="You are a teacher that create structured and clean curriculums",
    llm=model,
    verbose=True
)
formatter=Agent(
    role="Formatter",
    goal="Format the outputs into a clean and readable markdown file",
    backstory="You are a writer that makes content organized and readable",
    llm=model,
    verbose=True
)
user_input=input("What do you want to learn?")
analyze_task=Task(
    agent=analyer,
    description=f"Parse the user input:{user_input}",
    expected_output="JSON:{topic: string, level: string, goal: string}",
)
search_task=Task(
    agent=searcher,
    description=f"Find 4-5 free resources for the {analyze_task.expected_output["topic"]} in the {analyze_task.expected_output["level"]} level in order to help the user achieve their goal:{analyze_task.expected_output["goal"]}",
    expected_output="List:[{url: string, title: string, description: string}](4-5 items)",
)
design_task=Task(
    agent=designer,
    description=f"Create a 4 week learning path for the {analyze_task.expected_output["topic"]} from {analyze_task.expected_output["level"]} level to the goal:{analyze_task.expected_output["goal"]}",
    expected_output="List:[{week: int, title: string, topics: string, description: string}](4 items)",
    )
project_task=Task(
    agent=project,
    description=f"Generate 3-4 project ideas for the {analyze_task.expected_output["topic"]} in the {analyze_task.expected_output["level"]} level in order to help the user achieve their goal:{analyze_task.expected_output["goal"]}",
    expected_output="List:[{title: string, description: string}](3-4 items)",
)
formatter_task=Task(
    agent=formatter,
    description=f"Format the outputs into a clean and readable markdown file",
    expected_output="Markdown file with the following sections: Topic, Goal, Resources, Learning Path, Projects",
)
crew=Crew(
    agents=[analyer,searcher,project,designer,formatter],
    tasks=[analyze_task,search_task,design_task,project_task,formatter_task],
    verbose=2,
)
result=crew.kickoff()
with open("output.md", "w") as f:
    f.write(str(result))
print("Curriculum generated and saved to output.md")


