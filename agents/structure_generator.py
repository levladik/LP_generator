from agents import Agent, Runner
import asyncio
from .utils import load_environment, load_prompt

api_key = load_environment()

prompt_template = load_prompt('prompts/structure_generation.txt')

user_topic = input("Введите тему: ")

final_prompt = prompt_template.format(topic=user_topic,)

structure_generator_agent = Agent(
    name="Structure Generator",
    model="gpt-4o-mini",
)

async def main():
  result = await Runner.run(structure_generator_agent, final_prompt)
  print(result.final_output)

asyncio.run(main())
