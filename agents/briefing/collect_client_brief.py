import json

questions = [
    # General Information
    "What is the name of your company / product / brand?",
    "Do you already have a logo or should it be designed?",
    "What is the main goal of the landing page?",
    "What is the target audience? (age, gender, location, profession, interests)",
    "Do you have a domain name and hosting already?",
    "Do you have any examples of landing pages you like?",

    # Content & Structure
    "What is your main offer or value proposition?",
    "What problem does your product or service solve?",
    "What are the key benefits or features to highlight?",
    "Do you have a slogan or tagline?",
    "Will you need help writing the text (copywriting)?",
    "What sections should the page include? (Hero, Features, About, Testimonials, Pricing, FAQ, Contact form, CTA, etc.)",

    # Visuals & Branding
    "Do you have a brand style guide (colors, fonts, etc.)?",
    "Do you have any photos, videos, or illustrations you'd like to include?",
    "Should the design be minimal, playful, corporate, creative, or something else?",
    "Are there any colors or styles to avoid?",

    # Functionality
    "What should happen when a user clicks the main CTA button?",
    "Do you need to collect user data (e.g. form with email, phone)?",
    "Should the form integrate with any CRM or email marketing tool (like Mailchimp, HubSpot, etc.)?",
    "Do you need analytics or tracking (Google Analytics, Meta Pixel)?",
    "Should it support multiple languages?",

    # Timing & Budget
    "Do you have a deadline or launch date?",
    "What is your budget range for this project?",

    # Final Notes
    "Is there anything else I should know before starting?",
    "Who will be the main point of contact for feedback and approval?"
]

brief = {}

async def main():
  for question in questions:
      answer = input(question + " ")
      brief[question] = answer.strip()
  
  print("\nThank you! Here is your completed brief:")
  for q, a in brief.items():
      print(f"{q}\n- {a}\n")
  
  with open('client_brief.json', 'w') as f:
      json.dump(brief, f, indent=2)
  print("\nBrief saved to client_brief.json")
  return True
