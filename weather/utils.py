import functools
import os
import pathlib
import pickle
from datetime import datetime
from typing import Any, Callable


def cache(
    secs_to_expired: int = 0,
) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
    """
    Adds cache functionality with time expiration.
    Cache is stored in the current directory in the 'cache' folder.
    Caching state consists of last call time of a function and it's
    result. If time is expired, cache is rewritten with new state.
    """

    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            now = datetime.today()
            data, cached_time = None, None

            path = pathlib.Path(
                pathlib.Path(__file__).parent,
                'cache',
                str(args) + str(kwargs) + '.pickle',
            )

            # loads cache if it is
            if os.path.exists(path):
                with open(path, 'rb') as file:
                    data, cached_time = pickle.load(file)

            # checks data and expiration time
            if data is None or cached_time is None or (now - cached_time).seconds > secs_to_expired:
                data = func(*args)
                cached_time = now

            # writes the data and time of the function call in the cache
            with open(path, 'wb') as file:
                pickle.dump([data, cached_time], file)

            return data

        return wrapper

    return decorator
