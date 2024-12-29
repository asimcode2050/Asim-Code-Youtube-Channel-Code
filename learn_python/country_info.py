''' pip install countryinfo '''
from countryinfo import CountryInfo
def get_country_details(country_name: str):
    country = CountryInfo(country_name)
    country_info = country.info()
    if not country_info:
        return f"Sorry, we couldn't fetch details for {country_name}. Please check the country name and try again."

    capital = country_info.get("capital", "Not available")
    population = country_info.get("population", "Not available")
    currency = country_info.get("currency", "Not available")
    region = country_info.get("region", "Not available")
    return {
        "Country": country_name,
        "Capital": capital,
        "Population": population,
        "Currency": currency,
        "Region": region
    }

country_name = "Japan"
country_details = get_country_details(country_name)
print(country_details)
