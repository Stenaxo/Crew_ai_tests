from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import FileWriterTool, VisionTool
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SCRIPT_DIR = Path(__file__).parent
jpg_path = str(SCRIPT_DIR/"test.jpg")
jpg_search_tool = VisionTool()
file_writer_tool = FileWriterTool(output_dir=str(SCRIPT_DIR/"output"))

@CrewBase
class Papa():
    """Papa crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def jpg_rag_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['jpg_rag_agent'], # type: ignore[index]
            tools=[jpg_search_tool],
            verbose=True
        )

    @agent
    def jpg_summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['jpg_summary_agent'], # type: ignore[index]
            tools=[file_writer_tool],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def jpg_invoice_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['jpg_invoice_extraction_task'], # type: ignore[index]
        )

    @task
    def invoice_data_to_csv_task(self) -> Task:
        return Task(
            config=self.tasks_config['invoice_data_to_csv_task'], # type: ignore[index]
            output_file='tva.csv'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the jpgRag crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
