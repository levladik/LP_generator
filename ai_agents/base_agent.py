import os
from agents import Agent, Runner
from dotenv import load_dotenv
from typing import Type, Any

class BaseAgent():
    """
    Base class for AI-agents.
    Implements common methods for working with AI models.
    """
    def __init__(self, name: str, prompt: str, model: str='gpt-4.1-nano', output_type: Type[Any] = str):
        """
        Initializes the BaseAgent:

        :param name: Name of the agent.
        :param prompt: Prompt for the agent.
        :param model: Model name to use for the agent.
        """
        self.model = model
        self.name = name
        self.prompt = prompt
        self.output_type = output_type

    def _load_api_key(self):
        """Load AI API key from environment variables."""
        load_dotenv()
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variable.")
        return api_key

    async def generate_response(self):
        agent = Agent(
            name=self.name,
            model=self.model,
            instructions=self.prompt,
            output_type=self.output_type
        )
        
        result = await Runner.run(agent, self.prompt)
        return result.final_output
        
