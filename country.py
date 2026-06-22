class Country:
    def __init__(
        self,
        name: str,
        population: int,
        capital: str,
        region: str,
        flag: str,
        timezone: str,
        currency: str,
    ):
        self.name = name
        self.population = population
        self.capital = capital
        self.region = region
        self.flag = flag
        self.timezone = timezone
        self.currency = currency

    def __str__(self) -> str:
        return f"""
country: {self.name}
population: {self.population}
capital: {self.capital}
region: {self.region}
flag: {self.flag}
timezone: {self.timezone}
currencies: {self.currency}
"""