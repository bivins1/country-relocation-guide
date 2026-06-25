# from fetch_country import fetch_country
# from initialize_gemini import initialize_gemini
# from save_checklist import save_checklist


# def travel_checklist():

#     user_choice = input("what is the country name: ").strip()

#     travel_type = input("VACATION OR RELOCATION: ").strip().lower()


#     country_data = fetch_country(user_choice)
#     if not country_data:
#         return


#     try:
#         client = initialize_gemini()
#     except Exception as e:
#         print(f"Failed to initialize AI: {e}")
#         return


#     prompt = f"""
#     You are a travel assistant.

#     The user is travelling to {user_choice} for {travel_type}.

#     Using the provided country data, generate a simple, practical, and beginner friendly travel checklist.

#     Your checklist should include:

#     Required travel documents
#     Health precautions
#     Currency and payment readiness
#     Packing recommendations
#     Safety reminders
#     Travel tips specific to {travel_type}

#     Keep it concise and structured.

#     This is the provided country data:

#     {country_data}
#     """


#     print("\n--- Generating travel checklist ---\n")

#     response_text = ""


#     try:
#         response = client.models.generate_content(
#             model="gemini-3.5-flash",
#             contents=prompt
#         )
#         # Ensure response_text is always a string (response.text may be None)
#         response_text = response.text or ""
#         print(response_text)

#     except Exception as e:
#         print(f"error occurred: {e}")
#         return


#     save_choice = input("Do you want to save checklist? (yes/no): ").strip().lower()


#     if save_choice == "yes":
#         filename=f"{user_choice}.txt"
#         save_checklist(response_text, filename)

#     elif save_choice == "no":
#         print("Checklist discarded.")

#     else:
#         print("Invalid choice. Exiting.")



from fetch_country import fetch_country
from initialize_gemini import initialize_gemini


def travel_checklist(country_name, travel_type):

    country_data = fetch_country(country_name)
    if not country_data:
        return "Invalid country or data not found."

    try:
        client = initialize_gemini()
    except Exception as e:
        return f"Failed to initialize AI: {e}"

    prompt = f"""
    You are a travel assistant.

    The user is travelling to {country_name} for {travel_type}.

    Using the provided country data, generate a simple, practical travel checklist.

    Include:
    - Required documents
    - Health precautions
    - Currency/payment
    - Packing list
    - Safety tips
    - Travel advice

    Country data:
    {country_data}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text

    except Exception as e:
            raise RuntimeError(f"Error generating the guide: {e}") from e