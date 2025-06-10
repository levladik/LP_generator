from llama_index.llms.openai import OpenAI
import json
import asyncio

llm = OpenAI(model="gpt-4.1-nano")

questions = [
    "The purpose of the landing page (sales/leads/registrations)",
    "Target audience (demographics, pains, triggers)",
    "TSS and key benefits",
    "Desired structure (blocks)",
    "Brand guideline (colors, style)",
    "Examples of competitors",
    "Key CTAs",
]

brief = {}

async def main():
    print("Hi. Let's put together a brief for your website.")
for question in questions:
    print(f"\nAutoLander: {question}")
    
    user_input = input("You: ")
    
    brief[question] = user_input

    prompt = f"You're a professional interviewer to create landing pages. You asking this set of questions: '{questions}. This is user answewrs: {brief}. Right now you are asking this question: {question}. User answer is: '{user_input}'. Ask clarification question if you need to get more details about this answer. Do not ask about other questions, just ask about this one."
    ai_question = llm.complete(prompt).text
    print(f"\nnAutoLander: {ai_question}")
    
    clarification = input("You: ")
    brief[ai_question] = clarification

with open('brief.json', 'w') as f:
    json.dump(brief, f, indent=2, ensure_ascii=False)

print("\nThe brief has been saved to the brief.json file!")
    
if __name__ == "__main__":
    asyncio.run(main())
