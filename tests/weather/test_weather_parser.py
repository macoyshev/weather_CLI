import pytest

from weather.weather_parser import get_weather_for_city


@pytest.fixture()
def request_mock(mocker):
    return mocker.patch('weather.weather_parser.requests.get')


@pytest.mark.parametrize('city, expected_value', [('kazan', '-999°'), ('moscow', '-1000°'), ('orel', '+12°')])
def test_right_city(request_mock, city, expected_value):
    request_mock.return_value.text = f'<div id="weather-now-number">{expected_value}</div>'
    request_mock.return_value.status_code = 200

    assert expected_value == get_weather_for_city(city)


def test_wrong_city(request_mock):
    request_mock.return_value.status_code = 404

    with pytest.raises(RuntimeError):
        get_weather_for_city('iphone')
