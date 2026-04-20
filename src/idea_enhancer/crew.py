from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from idea_enhancer.tools.custom_tool import WebSearchTool
from idea_enhancer.tools.reddit_tool import RedditSearchTool


free_search = WebSearchTool()
reddit_search = RedditSearchTool()


# Define DelegationInput and DelegationTool
class DelegationInput(BaseModel):
    task: str = Field(..., description="The task to delegate to a coworker")
    context: str = Field("", description="Context for the delegation")


class DelegationTool(BaseTool):
    name: str = "delegate_work"
    description: str = "Delegate tasks to crew members: chief executive officer (ceo), chief technology officer (cto), chief financial officer (cfo), chief marketing officer (cmo)"
    args_schema: Type[BaseModel] = DelegationInput

    def _run(self, task: str, context: str = "") -> str:
        return f"Delegation tool executed with task: {task}, context: {context}"


@CrewBase
class IdeaEnhancer():
    """IdeaEnhancer crew for executive discussion"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- Agents ---

    @agent
    def ceo(self) -> Agent:
        return Agent(
            config=self.agents_config['ceo'],
            verbose=True,
            allow_delegation=True,
            human_input=True
        )

    @agent
    def cto(self) -> Agent:
        return Agent(
            config=self.agents_config['cto'],
            verbose=True,
            tools=[free_search]
        )

    @agent
    def cfo(self) -> Agent:
        return Agent(
            config=self.agents_config['cfo'],
            verbose=True,
            tools=[free_search]
        )

    @agent
    def cmo(self) -> Agent:
        return Agent(
            config=self.agents_config['cmo'],
            verbose=True,
            tools=[free_search, reddit_search]
        )

    # --- Tasks ---

    @task
    def initial_idea_critique(self) -> Task:
        return Task(
            config=self.tasks_config['initial_idea_critique'],
            human_input=True
        )

    @task
    def technical_and_market_validation(self) -> Task:
        return Task(
            config=self.tasks_config['technical_and_market_validation'],
            context=[self.initial_idea_critique()]
        )

    @task
    def final_project_blueprint(self) -> Task:
        return Task(
            config=self.tasks_config['final_project_blueprint'],
            output_file='enhanced_idea_report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.cto(), self.cfo(), self.cmo()],
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.ceo(),
            verbose=True,
            max_rpm=10,
            max_iter=7,
        )