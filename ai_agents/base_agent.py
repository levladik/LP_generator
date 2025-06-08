import os
from agents import Agent, Runner
from dotenv import load_dotenv

class BaseAgent():
    """
    Base class for AI-agents.
    Implements common methods for working with AI models.
    """
    def __init__(self, name, prompt, model='gpt-4o-mini'):
        """
        Initializes the BaseAgent:

        :param name: Name of the agent.
        :param prompt: Prompt for the agent.
        :param model: Model name to use for the agent.
        """
        self.model = model
        self.name = name
        self.prompt = prompt

    def _load_api_key(self):
        """Load AI API key from environment variables."""
        load_dotenv()
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variable.")
        return api_key

    def generate_response(self):
        agent = Agent(
            name=self.name,
            model=self.model,
            instructions=self.prompt
        )
        
        return Runner.run(agent, self.prompt)
        
