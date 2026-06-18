from fetch_country import fetch_country
from initialize_gemini import initialize_gemini

def travel_checklist():

    user_choice=input("what is the country name:").strip()

    country_data=fetch_country(user_choice)
    if not country_data:
        return

    try:
        client = initialize_gemini()
    except Exception as e:
        print(f"Failed to initialize AI: {e}")
        return

    prompt= f"""
    You are a travel assistant.

    Using the provided country data, generate a simple, practical, and concise travel preparation checklist for someone planning to either visit or relocate to the country.

    Your response should include the following sections:

    Required Documents (e.g., passport, visa, permits if applicable)
    Health Precautions (recommended vaccinations, health advice, or travel insurance)
    Currency & Payment Readiness (local currency, common payment methods, and useful financial tips)
    Safety Reminders (important safety advice and emergency considerations)
    Packing & Travel Tips (weather-appropriate clothing, essential items, and transportation tips)
    Local Customs & Important Regulations (basic cultural etiquette, important laws, or customs visitors should know)

    Keep the checklist easy to read by using bullet points. Tailor your recommendations to the specific country using the provided information, and avoid including information that is uncertain or unsupported by the country data.

    This is the provided country data:

{country_data}

"""
    response_text="no response please try again"

    try:
        response = client.models.generate_content(
                    model="gemini-3.5-flash", 
                    contents={prompt}
                )
        response_text=response.text
        print(response_text)

        
    except Exception as e:
        print(f"error occurred: {e}")

    return response_text


travel_checklist()

