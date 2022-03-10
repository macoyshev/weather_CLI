class RequestError(Exception):
    pass


class BadRequest(RequestError):  # status_code == HTTPStatus.BAD_REQUEST
    pass


class NotFound(RequestError):  # status_code == HTTPStatus.NOT_FOUND
    pass


class NotClientError(RequestError):
    pass


class NetworkError(NotClientError):  # requests.exception.connection
    pass


class ServerError(NotClientError):  # status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    pass
