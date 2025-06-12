import asyncio
from agents.briefing.collect_client_answers import main as collect_client_answers

async def main():
    await collect_client_answers()

if __name__ == "__main__":
    asyncio.run(main())
