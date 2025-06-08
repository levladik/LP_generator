from ai_agents.base_agent import BaseAgent
import asyncio

async def main():
    topic = input("Enter topic: ")
    prompt = (
        f"Your task is to create four block names for a landing page on the topic: {topic}.\n"
        "In your answer, write only the block names, without explanations.\n"
        "For example: 1. The name of block 1, 2. The name of block 2, 3. The name of block 3, 4. Name of block 4.\n"
    )

    StructureAgent = BaseAgent("Structure Generator", prompt)
    response = await StructureAgent.generate_response()
    return response

if __name__ == "__main__":
    asyncio.run(main())
