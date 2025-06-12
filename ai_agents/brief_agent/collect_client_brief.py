from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.workflow import Context

from ai_agents.brief_agent.tools.json_tool import save_brief_to_json

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

workflow = AgentWorkflow.from_tools_or_functions(
    tools_or_functions=[save_brief_to_json],
    llm=llm,
    system_prompt=f"You're a professional interviewer to create landing pages. You asking set of questions: '{questions} and put them inside '{brief}' in format question: answer. Ask one question at a time, and wait for the answer before asking the next question. If you have all the information you need, save it to a JSON file. Do not finish the interview until all questions are answered.",
)

ctx = Context(workflow)

async def main():
    result = await workflow.run(user_msg="Start interview", ctx=ctx)
    print(result)
