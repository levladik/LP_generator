from ai_agents.structure_generator import main as structure_generator
import asyncio

async def run_agents():
    generated_structure = await structure_generator()
    print(generated_structure)
    # Add other agents here as they're implemented

if __name__ == "__main__":
    asyncio.run(run_agents())
