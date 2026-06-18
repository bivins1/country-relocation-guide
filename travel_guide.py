from fetch_country import fetch_country
from initialize_gemini import initialize_gemini

def travel_guide():

    user_choice=input("what country:").strip()

    country_data=fetch_country(user_choice)

    client=initialize_gemini()

    prompt= f"""
    you are a travel assistant

    using the provided country data generate a simple and concise travel preparation checklist and travel guide for customers looking for relocation

    your output should include:
    documents needed
    health precautions
    travel tips
    currency readiness
    safety reminders

    this is the provided country data:
    {country_data}
"""
    response="no response please try again"

    try:
        response = client.models.generate_content(
                    model="gemini-3.5-flash", 
                    contents=f"{prompt}"
                )
        print(response.text)
    except Exception as e:
        print(f"error occurred: {e}")

    return response.text

travel_guide()

