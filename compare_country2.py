def compare_country(country1, country2):
    if country1['population'] > country2['population']:
        return f"{country1['name']} population is larger than {country2['name']}."
    elif country1['population'] < country2['population']:
        return f"{country2['name']} population is larger than {country1['name']}."
    else:
        return f"{country1['name']} and {country2['name']} have the same population."
    
    return {
        'population': 'population_result',
        'currency': f'{country1["currency"]} vs {country2["currency"]}',
        'language': f'{country1["language"]} vs {country2["language"]}',
        'area': f'{country1["area"]} vs {country2["area"]}',
        }
