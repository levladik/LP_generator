import json

def save_brief_to_json(brief):
    """
    Save the brief dictionary to a JSON file.
    """
    with open('brief.json', 'w') as f:
        json.dump(brief, f, indent=2, ensure_ascii=False)
