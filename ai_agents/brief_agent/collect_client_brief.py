from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.workflow import Context

from ai_agents.brief_agent.tools.question_tool import get_questions
from ai_agents.brief_agent.tools.json_tool import save_brief_to_json
from ai_agents.brief_agent.shared_state import brief

llm = OpenAI(model="gpt-4.1-nano")

workflow = AgentWorkflow.from_tools_or_functions(
    tools_or_functions=[get_questions, save_brief_to_json],
    llm=llm,
    system_prompt=f"You're a professional interviewer to create landing pages. You asking set of questions and put them inside '{brief}'. Ask one question at a time, and wait for the answer before asking the next question. If you have all the information you need, save it to a JSON file.",
)

ctx = Context(workflow)

async def main():
    result = await workflow.run(user_msg="Start interview", context=ctx)
    print(result)
