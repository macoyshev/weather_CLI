import functools
import os
import pathlib
import pickle
from datetime import datetime
from typing import Any, Callable


def cache(
    ttl: int = 0,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Adds cache functionality with time expiration.
    Cache is stored in the current directory in the 'cache' folder.
    Caching state consists of last call time of a function and it's
    result. If time is expired, cache is rewritten with new state.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            now = datetime.utcnow()
            data, cached_time = None, None

            cache_folder = pathlib.Path(pathlib.Path(__file__).parent, 'cache')
            cached_file = pathlib.Path(
                cache_folder,
                str(args) + str(kwargs) + '.pickle',
            )

            # create cache folder if it does not exists
            if not os.path.exists(cache_folder):
                os.mkdir(cache_folder)

            # loads cache if it is
            if os.path.exists(cached_file):
                with open(cached_file, 'rb') as file:
                    data, cached_time = pickle.load(file)

            # if cache file does not exists or time is expired, then data and cached time is updated
            if data is None or cached_time is None or (now - cached_time).total_seconds() > ttl:
                data = func(*args, **kwargs)
                cached_time = now

            # writes data and time call of the function in the cache
            with open(cached_file, 'wb') as file:
                pickle.dump([data, cached_time], file)

            return data

        return wrapper

    return decorator
