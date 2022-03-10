import pytest

from weather.exceptions import NotClientError, RequestError
from weather.weather_parser import get_weather_for_city


@pytest.mark.usefixtures('_response_with_200', 'delete_cache_per_one_test')
@pytest.mark.parametrize(('city', 'expected_value'), [('kazan', '-9°'), ('moscow', '-10°')])
def test_right_city(req_mock, city, expected_value):
    assert expected_value == get_weather_for_city(city)
    req_mock.assert_called_once_with(f'https://world-weather.ru/pogoda/russia/{city}')


@pytest.mark.usefixtures('_response_with_200', 'delete_cache_after_tests')
@pytest.mark.parametrize(('city', 'expected_value'), [('kazan', '-9°'), ('kazan', '-9°')])
def test_right_city_from_cache(city, expected_value):
    assert expected_value == get_weather_for_city(city)


@pytest.mark.usefixtures('_response_with_404')
def test_wrong_city():
    with pytest.raises(RequestError):
        get_weather_for_city('iphone')


@pytest.mark.usefixtures('_response_with_500')
def test_server_error():
    with pytest.raises(NotClientError):
        get_weather_for_city('moscow')


@pytest.mark.usefixtures('_response_with_404')
def test_wrong_city(req_mock):
    with pytest.raises(RequestError):
        get_weather_for_city('iphone')
