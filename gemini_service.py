import json
import os
import google.generativeai as genai

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "services.json")

with open(json_path, "r") as f:
    services = json.load(f)

genai.configure(api_key=services["GEMINI_API_KEY"])

def get_gemini_response(prompt):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
