import pytest

from weather.weather_parser import get_weather_for_city


@pytest.mark.parametrize(('city', 'expected_value'), [('kazan', '-9°'), ('moscow', '-10°')])
def test_right_city(req_mock, city, expected_value):
    req_mock.return_value.text = f'<div id="weather-now-number">{expected_value}</div>'
    req_mock.return_value.status_code = 200

    assert expected_value == get_weather_for_city(city)


def test_wrong_city(req_mock):
    req_mock.return_value.status_code = 404

    with pytest.raises(RuntimeError):
        get_weather_for_city('iphone')
