import shutil

import requests
import pytest


@pytest.fixture()
def req_mock(mocker):
    return mocker.patch('weather.weather_parser.requests.get')


@pytest.fixture()
def _response_with_200(req_mock, expected_value):
    req_mock.return_value.text = f'<div id="weather-now-number">{expected_value}</div>'
    req_mock.return_value.status_code = 200


@pytest.fixture()
def _response_with_404(req_mock):
    mock_resp = requests.models.Response()
    mock_resp.status_code = 404
    req_mock.return_value = mock_resp


@pytest.fixture()
def _response_with_500(req_mock):
    mock_resp = requests.models.Response()
    mock_resp.status_code = 500
    req_mock.return_value = mock_resp


@pytest.fixture()
def delete_cache_per_one_test():
    yield
    shutil.rmtree('weather/cache')


@pytest.fixture(scope='session')
def delete_cache_after_tests():
    yield
    shutil.rmtree('weather/cache')
