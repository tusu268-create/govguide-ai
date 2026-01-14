import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

with open("services.json", "r") as f:
    services = json.load(f)

def ask_gemini(user_query, agent_fee):
    prompt = f"""
You are an AI government service assistant.

User question: {user_query}
Agent fee asked: ₹{agent_fee}

Official government services data:
{services}

Tasks:
1. Identify the service
2. Explain steps simply
3. Check if agent fee is fraud or genuine
4. Share official website
"""
    response = model.generate_content(prompt)
    return response.text
