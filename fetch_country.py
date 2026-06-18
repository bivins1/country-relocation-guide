import re
import requests
from dotenv import load_dotenv
import os


load_dotenv()
pattern = r"[A-Za-z]+([ -'][A-Za-z]+)*"


def fetch_country(country_choice):
    if not re.fullmatch(pattern, country_choice):
        print("invalid country name")
        return
    
    rest_api=os.getenv("REST_API")
    headers = {"Authorization": rest_api}
    url = f"https://api.restcountries.com/countries/v5/names.common/{country_choice}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()

        country_object = result.get("data", {}).get("objects", [])

        if not country_object:
            print("country selected does not exist")
            return

        country = country_object[0]

        name = country.get("names", {})
        if not name:
            country_name = "country name does not exist"
            print("country has no name")
        else:
            country_name = name.get("common", "unknown")
        # print(country_name)

        # print(country.get("population", 0))

        capital = country.get("capitals", [])
        if capital:
            capital_name = capital[0].get("name", "unknown")
            # print(capital_name)
        else:
            capital_name = "no capital"
            # print("country has no capital")

        # print(country.get("region", "unknown"))

        flag = country.get("flag", {}).get("emoji", "no flag")
        # print(flag)

        timezone = ", ".join(country.get("timezones", []))
        # print(timezone)

        currencies = country.get("currencies", [])
        if currencies:
            currency_name = currencies[0].get("name", "unknown")
            # print(currency_name)
        else:
            currency_name = "no currency"
            # print("No currency")

        country_data = f"""
country:{country_name}
population:{country.get("population", 0)}
capital:{capital_name}
region:{country.get("region", "unknown")}
flag:{flag}
timezone:{timezone}
currencies:{currency_name}
"""
        return country_data
        

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        print(e.response.text)
        return

    except requests.exceptions.RequestException as error:
        print(f"Request error: {type(error)}")
        return
    
