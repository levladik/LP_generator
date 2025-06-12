import json
from ai_agents.brief_agent.shared_state import brief

def save_brief_to_json():
    """
    Save the brief dictionary to a JSON file.
    """
    with open('brief.json', 'w') as f:
        json.dump(brief, f, indent=2, ensure_ascii=False)
