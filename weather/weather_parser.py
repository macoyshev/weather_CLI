import requests
from bs4 import BeautifulSoup

from weather.utils import cache


@cache(secs_to_expired=1)
def get_weather_for_city(city: str) -> str:
    """
    Returns temperature of the city in celsius,
    as the source 'https://world-weather.ru' was used
    """

    url = f'https://world-weather.ru/pogoda/russia/{city}'

    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError('bad request')

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.find('div', id='weather-now-number').text
