from fetch_country import fetch_country
from initialize_gemini import initialize_gemini


def travel_checklist():

    user_choice = input("what is the country name: ").strip()

    travel_type = input("VACATION OR RELOCATION: ").strip().lower()


    country_data = fetch_country(user_choice)
    if not country_data:
        return


    try:
        client = initialize_gemini()
    except Exception as e:
        print(f"Failed to initialize AI: {e}")
        return


    prompt = f"""
    You are a travel assistant.

    The user is travelling to {user_choice} for {travel_type}.

    Using the provided country data, generate a simple, practical, and beginner friendly travel checklist.

    Your checklist should include:

    Required travel documents
    Health precautions
    Currency and payment readiness
    Packing recommendations
    Safety reminders
    Travel tips specific to {travel_type}

    Keep it concise and structured.

    This is the provided country data:

    {country_data}
    """


    print("\n--- Generating travel checklist ---\n")

    response_text = ""


    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        response_text = response.text
        print(response_text)

    except Exception as e:
        print(f"error occurred: {e}")
        return


    save_checklist = input("Do you want to save checklist? (yes/no): ").strip().lower()


    if save_checklist == "yes":
        save_guide(response_text)

    elif save_checklist == "no":
        print("Checklist discarded.")

    else:
        print("Invalid choice. Exiting.")


travel_checklist()