import pytest


@pytest.fixture()
def req_mock(mocker):
    return mocker.patch('weather.weather_parser.requests.get')
