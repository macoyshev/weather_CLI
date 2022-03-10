import http

import requests
import tenacity
from bs4 import BeautifulSoup
from tenacity import retry_if_exception_type, stop_after_attempt

from .exceptions import BadRequest, NetworkError, NotClientError, NotFound, ServerError
from .utils import cache


@tenacity.retry(
    reraise=True,
    retry=retry_if_exception_type(NotClientError),
    stop=stop_after_attempt(5),
)
@cache(ttl=1)
def get_weather_for_city(city: str) -> str:
    """
    Returns temperature of the city in celsius,
    as the source 'https://world-weather.ru' was used
    """

    url = f'https://world-weather.ru/pogoda/russia/{city}'
    page_text = None

    try:
        response = requests.get(url)
        response.raise_for_status()

        page_text = response.text
    except requests.exceptions.HTTPError as err:
        err_status = err.response.status_code

        if err_status == http.HTTPStatus.BAD_REQUEST:
            raise BadRequest() from None

        if err_status == http.HTTPStatus.NOT_FOUND:
            raise NotFound() from None

        if err_status == http.HTTPStatus.INTERNAL_SERVER_ERROR:
            raise ServerError from None

    except requests.exceptions.ConnectionError:
        raise NetworkError from None

    soup = BeautifulSoup(page_text, 'html.parser')

    return soup.find('div', id='weather-now-number').text
