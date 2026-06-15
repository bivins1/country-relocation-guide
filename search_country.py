import re
import requests



pattern=r"[A-Za-z]+([ -'][A-Za-z]+)*"

def country_search():
    country = input("what is the country name: ").strip()

    if not re.fullmatch(pattern, country):
        print("invalid country name")
        return
    
    params={
        "q":country
    }
    headers={'Authorization': 'Bearer rc_live_b04495913d254556bd142eeda6248825'}
    url="https://api.restcountries.com/countries/v5"
    response= requests.get(url, headers=headers)

    print(response.json())
    # try:
    #     country_check=requests.get(url, params=params, timeout=10, headers=headers)
    #     country_check.raise_for_status()

    #     print()


country_search()



    