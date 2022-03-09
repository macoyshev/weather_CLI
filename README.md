# WeatherRU
The console application that allows 
to find out the weather in any city in Russia.
Requests are cached, which allows to quickly
get up-to-date weather information. 
### Running application
To run the application execute the following command:
```sh
$ python -m weather city
```
Where __*city*__ is an arbitrary city in Russia, as in example:

![img.png](images/img.png)

##### Requirements
You must have `Python 3.8+` and
the following external libraries:
- `typer `
- `bs4`
- `requests`

