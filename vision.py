import os

from dotenv import load_dotenv

import google.generativeai as genai



# Load API key

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# Use the CORRECT model name for Gemini 1.5 Pro

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")



def ask_question(question):

    try:

        response = model.generate_content(question)

        return response.text

    except Exception as e:

        return f"Error from Gemini API: {str(e)}"
