from dotenv import load_dotenv
from fetch_country import fetch_country
from initialize_gemini import initialize_gemini

load_dotenv()

def country_search():
    country_choice = input("what is the country name: ").strip()

    country_data=fetch_country(country_choice)

    client=initialize_gemini()

    prompt1=f"""

    you are a vacation assistant.

    generate a simple travel guide for people looking to have a vacation using the provided country data.

    use this structure when providing your answer:
    -overview
    -culture
    -country landmarks
    -travel tips

    this is the provided country data:
    {country_data}
"""
    prompt2=f"""

    you are a  relocation assistant.

    generate a simple travel guide for people looking to relocate using the provided country data.

    use this structure when providing your answer:
    -overview
    -cost of living
    -culture
    -security
    -travel tips

    this is the provided country data:
    {country_data}

"""
    
    user_choice=input("please choose one, VACATION OR RELOCATION:").strip()

    try:
        if not user_choice:
            print("no choice made cannot proceed. please make a choice.")
            return
        elif  not (user_choice.lower()=="vacation" or user_choice.lower()=="relocation"):
            print("invalid option")
        elif user_choice.lower() == "vacation":
            response = client.models.generate_content(
                model="gemini-3.5-flash", 
                contents=f"{prompt1}"
            )
            print(response.text)
        elif user_choice.lower() == "relocation":
            response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"{prompt2}"
        )
            print(response.text)
    except Exception as e:
        print(f"error: {e} encountered")

    return
    


country_search()
