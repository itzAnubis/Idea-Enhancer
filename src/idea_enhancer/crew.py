from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from idea_enhancer.tools.custom_tool import WebSearchTool


free_search = WebSearchTool()

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
            allow_delegation=True 
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
            tools=[free_search]
        )

    # --- Tasks ---

    @task
    def initial_idea_critique(self) -> Task:
        return Task(
            config=self.tasks_config['initial_idea_critique'],
            human_input=True # This allows the CEO to ask you questions
        )

    @task
    def technical_and_market_validation(self) -> Task:
        return Task(
            config=self.tasks_config['technical_and_market_validation'],
            context=[self.initial_idea_critique()] # Passes CEO notes to others
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
            agents=self.agents,  # Auto-includes all @agent methods
            tasks=self.tasks,
            process=Process.sequential,  # Eliminates delegation routing bugs
            verbose=True,
            cache=True,
            max_rpm=10,          # Prevents OpenRouter 429s
            max_iter=7,
            memory=False         # Saves context window
        )