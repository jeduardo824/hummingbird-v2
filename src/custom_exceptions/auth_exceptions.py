from werkzeug.exceptions import HTTPException


class UnauthorizedException(HTTPException):
    """
    Base HTTPException for UNAUTHORIZED - 401 requests
    You should extend new classes in this file bellow
    and setup a custom description.
    The status code should remains the same
    """
    def __init__(self):
        super(HTTPException, self).__init__()
        self.code = 401


class BadUsernameOrPassword(UnauthorizedException):
    description = 'Bad username or password'
