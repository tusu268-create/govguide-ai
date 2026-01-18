import google.generativeai as genai
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load API key
with open(os.path.join(BASE_DIR, "services.json"), "r") as f:
    data = json.load(f)

API_KEY = data.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in services.json")

genai.configure(api_key=API_KEY)

def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash"
        )
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text
        else:
            return "No explanation available right now."

    except Exception as e:
        # IMPORTANT: never crash the app
        return "AI explanation service is temporarily unavailable."
