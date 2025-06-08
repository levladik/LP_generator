import os
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()
    return os.environ.get("OPENAI_API_KEY")

def load_prompt(path):
    """Load prompt template from file"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
