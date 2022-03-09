import typer

from weather.weather_parser import get_weather_for_city


def weather(city: str) -> None:
    try:
        temp = get_weather_for_city(city)
        typer.echo(f'Current weather in {city}: {temp}')
    except RuntimeError:
        typer.echo('Error: city does not exist')


if __name__ == '__main__':
    typer.run(weather)
