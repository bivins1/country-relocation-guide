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
    response= requests.get(url, headers=headers, )
    result=response.json()
    print(type(result))
    print(result.keys())
    # print(result["data"])
    # print(result["data"]["objects"])
    # print(type(result["data"]["objects"][0]))
    print(result["data"]["objects"][0].keys())
    print(result["data"]["objects"][0]["names"]["common"])
    print(result["data"]["objects"][0]["population"])
    print(result["data"]["objects"][0]["capitals"][0]["name"])
    print(result["data"]["objects"][0]["region"])
    print(result["data"]["objects"][0]["flag"]["emoji"])
    print(result["data"]["objects"][0]["timezones"])
    print(result["data"]["objects"][0]["currencies"][0]["name"])

    

    
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



    