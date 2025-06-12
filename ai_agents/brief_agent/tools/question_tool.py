from typing import List

questions: List[str] = [
    "The purpose of the landing page (sales/leads/registrations)",
    "Target audience (demographics, pains, triggers)",
    "TSS and key benefits",
    "Desired structure (blocks)",
    "Brand guideline (colors, style)",
    "Examples of competitors",
    "Key CTAs",
]

def get_questions(qstn_idx: int) -> str:
    """
    Function to get questions for the user to answer.
    """
    print(f"\nAutoLander: {questions[qstn_idx]}")
    user_input = input("You: ")
    return user_input
