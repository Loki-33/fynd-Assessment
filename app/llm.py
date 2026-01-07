import requests 
import os 
import re
from dotenv import load_dotenv
load_dotenv() 

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    print("ERROR: OPENROUTER_API_KEY not found!!!")
else:
    print("API KEY LOADED SUCCESSFULLY")
URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "AI Feedback System",
}

def generate_ai_outputs(review: str):
    prompt = f"""
User review:
"{review}"

Generate:
RESPONSE: friendly reply to user
SUMMARY: short internal summary
ACTIONS: recommended internal actions
"""

    payload = {
        "model": "nvidia/nemotron-3-nano-30b-a3b:free",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 300
    }

    try:
        res = requests.post(URL, headers=HEADERS, json=payload, timeout=15)
        res.raise_for_status()
        text = res.json()["choices"][0]["message"]["content"]
        print(text)
        
        def extract_sections(text: str) -> dict:
            patterns = {
                "response": r"(?:\*\*)?RESPONSE(?:\*\*)?:\s*(.*?)(?=\n\s*(?:\*\*)?SUMMARY(?:\*\*)?:)",
                "summary": r"(?:\*\*)?SUMMARY(?:\*\*)?:\s*(.*?)(?=\n\s*(?:\*\*)?ACTIONS(?:\*\*)?:)",
                "actions": r"(?:\*\*)?ACTIONS(?:\*\*)?:\s*(.*)$",
            }

            result = {}

            for key, pattern in patterns.items():
                match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
                if not match:
                    raise ValueError(f"Missing section: {key}")
                result[key] = match.group(1).strip()

            return result
        data = extract_sections(text)
        return {
            "ai_response": data['response'],
            "ai_summary": data['summary'],
            "ai_actions": data['actions']
        }

    except Exception as e:
        print("OpenRouter error:", e)
        return {
            "ai_response": "Thanks for your feedback! Our team will review it shortly.",
            "ai_summary": "AI unavailable",
            "ai_actions": "Manual review required"
        }


#def generate_ai_outputs(review: str):
#    try:
#        return {
#            "ai_response": "Thanks for your feedback! We really appreciate it.",
#            "ai_summary": "User provided feedback on product experience.",
#            "ai_actions": "Review feedback and consider improvements."
#        }
#    except Exception:
#        return {
#            "ai_response": "Thanks for your feedback! Our team will review it shortly.",
#            "ai_summary": "AI unavailable",
#            "ai_actions": "Manual follow-up required"
#        }
#
