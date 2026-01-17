import json
import os
import google.generativeai as genai

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load API key
with open(os.path.join(BASE_DIR, "config.json"), "r") as f:
    config = json.load(f)

genai.configure(api_key=config["GEMINI_API_KEY"])

def get_gemini_response(prompt):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
