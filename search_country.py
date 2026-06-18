
from dotenv import load_dotenv
from fetch_country import fetch_country
from initialize_gemini import initialize_gemini
from generate_guide import generate_country_guide

load_dotenv()

def country_search():
    # 1. Get Country Input
    country_choice = input("What is the country name: ").strip()
    if not country_choice:
        print("No country entered. Exiting.")
        return

    # 2. Fetch Data
    country_data = fetch_country(country_choice)
    if not country_data:
        return # fetch_country already prints the error message

    # 3. Initialize AI
    try:
        client = initialize_gemini()
    except Exception as e:
        print(f"Failed to initialize AI: {e}")
        return

    # 4. Get User Choice (Added 'Study' to the options)
    print("\nAvailable Guides: VACATION, RELOCATION, STUDY")
    user_choice = input("Please choose one: ").strip().lower()

    if not user_choice:
        print("No choice made. Cannot proceed.")
        return
        
    if user_choice not in ["vacation", "relocation", "study"]:
        print("Invalid option. Please type vacation, relocation, or study.")
        return

    # 5. Generate and Print the Guide
    print(f"\n--- Generating {user_choice.title()} Guide ---\n")
    
    try:
        guide_result = generate_country_guide(client, country_data, user_choice)
        print(guide_result)
        return guide_result
    except Exception as e:
        print(f"Error: {e} encountered during guide generation.")

country_search()