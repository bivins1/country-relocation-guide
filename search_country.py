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
    country_name = input("what is the country name: ").strip()

    if not re.fullmatch(pattern, country_name):
        print("invalid country name")
        return

    headers = {"Authorization": "Bearer rc_live_b04495913d254556bd142eeda6248825"}
    url = f"https://api.restcountries.com/countries/v5/names.common/{country_name}"

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

        print(country.get("names", {}).get("common", "unknown"))
        print(country.get("population", 0))

        capital = country.get("capitals", [])
        if capital:
            print(capital[0].get("name", "unknown"))
        else:
            print("country has no capital")

        print(country.get("region", "unknown"))
        print(country.get("flag", {}).get("emoji", "no flag"))

        print(", ".join(country.get("timezones", [])))

        currencies = country.get("currencies", [])
        if currencies:
            print(currencies[0].get("name", "unknown"))
        else:
            print("No currency")


        country_data=f"""

          country:{country.get("names", {}).get("common", "unknown")}
          population:{country.get("population", 0)}
          capital:{country.get("capitals", [])[0].get("name", "unknown")}
          region:{country.get("region", "unknown")}
          flag:{country.get("flag", {}).get("emoji", "no flag")}
          timezone:{", ".join(country.get("timezones", []))}
          currencies:{country.get("currencies", [])[0].get("name", "unknown")}
    """

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        print(e.response.text)

    except requests.exceptions.RequestException as error:
        print(f"Request error: {type(error)}")



    country_data

    prompt1=f"""

    you are a travel and relocation assistant.

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

    you are a travel and relocation assistant.

    generate a simple travel guide for people looking to have a relocate using the provided country data.

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

    if user_choice.lower() == "":
        print("no choice made cannot proceed. please make a choice.")
        return
    elif user_choice.lower() == "vacation":
        response = client.models.generate_content(
            model="gemini-3.5-flash", 
            contents=F"{prompt1}"
        )
        print(response.text)
    elif user_choice.lower() == "relocation":
        response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=F"{prompt2}"
    )
        print(response.text)
        
    

country_search()


