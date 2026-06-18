from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

def initialize_gemini():
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("api key not found")

    print(f"key loaded successfully {api_key [:4]}")

    client = genai.Client(api_key=api_key)
    return client
