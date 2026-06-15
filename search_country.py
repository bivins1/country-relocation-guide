import re
import requests

pattern=r"[A-Za-z]+([ -'][A-Za-z]+)*"

def country_search():
    country = input("what is the country name: ").strip()

    if not re.fullmatch(pattern, country):
        print("invalid country name")
        return
    
    headers={'Authorization': 'Bearer rc_live_b04495913d254556bd142eeda6248825'}
    url=f"https://api.restcountries.com/countries/v5/names.common/{country}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()

        country_object = result["data"]["objects"]

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

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        print(e.response.text)

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

country_search()



    