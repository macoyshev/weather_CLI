import typer

from .exceptions import NotClientError, RequestError
from .weather_parser import get_weather_for_city


def weather(city: str) -> None:
    try:
        temp = get_weather_for_city(city)
        typer.echo(f'Current weather in {city}: {temp}')
    except NotClientError:
        typer.echo('Error: please try later')
    except RequestError:
        typer.echo('Error: city does not exist')


if __name__ == '__main__':
    typer.run(weather)
