
from dotenv import load_dotenv
from fetch_country import fetch_country
from initialize_gemini import initialize_gemini
from generate_guide import generate_country_guide
from save_guide import save_guide

load_dotenv()

def country_search():
    
    country_choice = input("What is the country name: ").strip()
    if not country_choice:
        print("No country entered. Exiting.")
        return

    
    country_data = fetch_country(country_choice)
    if not country_data:
        return 
    else:
        print(country_data)

    try:
        client = initialize_gemini()
    except Exception as e:
        print(f"Failed to initialize AI: {e}")
        return

    print("\nAvailable Guides: VACATION, RELOCATION, STUDY")
    user_choice = input("Please choose one: ").strip().lower()

    if not user_choice:
        print("No choice made. Cannot proceed.")
        return
        
    if user_choice not in ["vacation", "relocation", "study"]:
        print("Invalid option. Please type vacation, relocation, or study.")
        return

    print(f"\n--- Generating {user_choice.title()} Guide ---\n")

    guide_result="" 
    
    try:
        guide_result = generate_country_guide(client, country_data, user_choice)
        print(guide_result)
        

    except Exception as e:
        print(f"Error: {e} encountered during guide generation.")
        return

    save_choice = input("Do you want to save guide? (yes/no): ").strip().lower()


    if save_choice == "yes":
        filename=f"{country_choice}.txt"
        save_guide(guide_result, filename)

    elif save_choice == "no":
        print("Checklist discarded.")

    else:
        print("Invalid choice. Exiting.")


    
