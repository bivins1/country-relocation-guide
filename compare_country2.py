from google.generativeai import genai
from fetch_country import fetch_country 
from initialize_gemini import GEMINI_API_KEY

def compare_countries(country1_name, country2_name):

    country1 = fetch_country(country1_name)
    country2 = fetch_country(country2_name)

    prompt = f"""
    Compare the following countries.

    Country 1:
    {country1}

    Country 2:
    {country2}

    Give:
    1. Overview
    2. Similarities
    3. Differences
    4. Travel comparison
    5. Study comparison
    6. Relocation comparison
    7. Final recommendation

    Keep the response concise and professional.
    """

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(prompt)

    return response.text
