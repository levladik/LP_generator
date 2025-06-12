import asyncio
from ai_agents.brief_agent.collect_client_brief import main as collect_client_brief


async def main():
    await collect_client_brief()

if __name__ == "__main__":
    asyncio.run(main())
