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

        response= requests.get(url, headers=headers )
        response.raise_for_status()
        result=response.json()

        print(type(result))
        # print(result.keys())
        # print(result["data"])
        print(type(result["data"]["objects"]))
        print(type(result["data"]["objects"]))
        print(result["data"]["objects"])



        country_object=result["data"]["objects"]

        if not country_object:
            print("country selected does not exist")
            return

        print(country_object[0].get("names", {}).get("common", "unknown"))
        print(country_object[0].get("population", 0))
        capital=country_object[0].get("capitals", [])
        print(capital[0].get("name", "unknown") if capital else "country has no capital" )
        print(country_object[0].get("region", "unknown"))
        print(country_object[0].get("flag", {}).get("emoji", "no flag"))
        print(", ".join(country_object[0].get("timezones", [])))
        currencies = country_object[0].get("currencies", [])

        print(currencies[0].get("name", "unknown") if currencies else "No currency")

    except requests.exceptions.HTTPError as e:
        print(f"error status code: {e.response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"error occured: {type(error)}")

   
       

    

    
    # print(result)
    # print(type(result["data"]["objects"]))
    # print(type(result["data"]["objects"][0]))
    # print(result["data"]["objects"][0].keys())

    # print(result["data"]["objects"][0]["names"]["common"])
    # print(result["data"]["objects"][0]["population"])
    # print(result["data"]["objects"][0]["capitals"][0]["name"])
    # print(result["data"]["objects"][0]["region"])
    # print(result["data"]["objects"][0]["flag"]["emoji"])
    # print(result["data"]["objects"][0]["timezones"])
    # print(result["data"]["objects"][0]["currencies"][0]["name"])

    

    # try:
    #     country_check=requests.get(url, params=params, timeout=10, headers=headers)
    #     country_check.raise_for_status()

    #     print()


country_search()



    