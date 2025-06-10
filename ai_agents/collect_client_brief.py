from ai_agents.base_agent import BaseAgent
import asyncio

async def main():
    prompt = (
        """You're a professional interviewer to create landing pages. Ask questions one at a time:
        1. The purpose of the landing page (sales/leads/registrations)
        2. Target audience (demographics, pains, triggers)
        3. TSS and key benefits
        4. Desired structure (blocks)
        5. Brand guideline (colors, style)
        6. Examples of competitors
        7. Key CTAs
        After each response, elaborate on the details. Organize the collected data into JSON with the keys: {goal, audience, usp, benefits, structure_preferences, brand_guidelines, competitors, ctas}."""
    )

    StructureAgent = BaseAgent("Structure Generator", prompt)
    response = await StructureAgent.generate_response()
    return response

if __name__ == "__main__":
    asyncio.run(main())
