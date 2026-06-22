import re
import requests
from dotenv import load_dotenv
import os

load_dotenv()

pattern = r"[A-Za-z]+([ -'][A-Za-z]+)*"


def fetch_country(country_choice: str) -> str | None:
    if not re.fullmatch(pattern, country_choice):
        print("invalid country name")
        return None

    rest_api = os.getenv("REST_API")

    if rest_api is None:
        raise ValueError("REST_API environment variable is not set")

    headers = {"Authorization": rest_api}

    url = f"https://api.restcountries.com/countries/v5/names.common/{country_choice}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()

        country_object = result.get("data", {}).get("objects", [])

        if not country_object:
            print("country selected does not exist")
            return None

        country = country_object[0]

        name = country.get("names", {})
        if not name:
            country_name = "country name does not exist"
            print("country has no name")
        else:
            country_name = name.get("common", "unknown")

        capital = country.get("capitals", [])
        if capital:
            capital_name = capital[0].get("name", "unknown")
        else:
            capital_name = "no capital"

        flag = country.get("flag", {}).get("emoji", "no flag")

        timezone = ", ".join(country.get("timezones", []))

        currencies = country.get("currencies", [])
        if currencies:
            currency_name = currencies[0].get("name", "unknown")
        else:
            currency_name = "no currency"

        country_data = f"""
country: {country_name}
population: {country.get("population", 0)}
capital: {capital_name}
region: {country.get("region", "unknown")}
flag: {flag}
timezone: {timezone}
currencies: {currency_name}
"""

        return country_data

    except requests.exceptions.HTTPError as e:
        if e.response is not None:
            print(f"HTTP error: {e.response.status_code}")
            print(e.response.text)
        else:
            print("HTTP error occurred but no response object")
        return None

    except requests.exceptions.RequestException as error:
        print(f"Request error: {type(error)}")
        return None