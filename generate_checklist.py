from fetch_country import fetch_country
from initialize_gemini import initialize_gemini
from save_guide import save_guide


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
        # Ensure response_text is always a string (response.text may be None)
        response_text = response.text or ""
        print(response_text)

    except Exception as e:
        print(f"error occurred: {e}")
        return


    save_checklist = input("Do you want to save checklist? (yes/no): ").strip().lower()


    if save_checklist == "yes":
        filename=f"{user_choice}.txt"
        save_guide(response_text, filename)

    elif save_checklist == "no":
        print("Checklist discarded.")

    else:
        print("Invalid choice. Exiting.")


travel_checklist()