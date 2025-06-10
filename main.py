from ai_agents.collect_client_brief import main as collect_client_brief
import asyncio

async def run_agents():
    client_brief = await collect_client_brief()
    print(client_brief)
    # Add other agents here as they're implemented

if __name__ == "__main__":
    asyncio.run(run_agents())
