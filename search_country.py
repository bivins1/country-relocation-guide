import re
import requests
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("api key not found")

print(f"key loaded successfully {api_key [:4]}")

client = genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model="gemini-3.5-flash", contents="Explain Nigeria in simple terms for a student."
# )

# print(response.text)

pattern = r"[A-Za-z]+([ -'][A-Za-z]+)*"


def country_search():
    country_choice = input("what is the country name: ").strip()

    if not re.fullmatch(pattern, country_choice):
        print("invalid country name")
        return

    headers = {"Authorization": "Bearer rc_live_b04495913d254556bd142eeda6248825"}
    url = f"https://api.restcountries.com/countries/v5/names.common/{country_choice}"

    country_data=""

    try:
        response = requests.get(
            url,
            headers=headers,
        )
        response.raise_for_status()
        result = response.json()

        country_object = result.get("data", {}).get("objects", [])

        if not country_object:
            print("country selected does not exist")
            return

        country = country_object[0]

        name=country.get("names", {})
        if not name:
            country_name="country name does not exist"
            print("country has no name")
        else: 
            country_name=name.get("common", "unknown")
        print(country_name)

        print(country.get("population", 0))

        capital = country.get("capitals", [])
        if capital:
            capital_name=capital[0].get("name", "unknown")
            print(capital_name)
        else:
            capital_name="no capital"
            print("country has no capital")

        print(country.get("region", "unknown"))

        flag=country.get("flag", {}).get("emoji", "no flag")
        print(flag)

        timezone= ", ".join(country.get("timezones", []))   
        print(timezone)

        currencies = country.get("currencies", [])
        if currencies:
            currency_name=currencies[0].get("name", "unknown")
            print(currency_name)
        else:
            currency_name="no currency"
            print("No currency")


        country_data=f"""

        country:{country_name}
        population:{country.get("population", 0)}
        capital: {capital_name}
        region:{country.get("region", "unknown")}
        flag:{flag}
        timezone:{timezone}
        currencies:{currency_name}
    """

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        print(e.response.text)
        return

    except requests.exceptions.RequestException as error:
        print(f"Request error: {type(error)}")
        return


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
    
country_search()


