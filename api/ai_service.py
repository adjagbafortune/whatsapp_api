import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_ai_response(messages):
    try:
        model = genai.GenerativeModel("gemini-1.0-pro")
        
        prompt = ""
        for msg in messages:
            prompt += f"{msg['role'].upper()}: {msg['content']}\n\n"
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f'{{"error": "Erreur Gemini: {str(e)}"}}'