from typing import Any,Callable
from fastapi.requests import Request
from fastapi.responses import JSONResponse


class BooklyException(Exception):
    """This is the base class for all bookly errors"""

    pass

class InvalidToken(BooklyException):
    """"User has provided an invalid or expired token"""
    pass

class RevokedToken(BooklyException):
    """User has provided a token that has been revoked"""
    pass

class AccessTokenRequired(BooklyException):
    """User has provided an refresh token when a access token is needed"""
    pass

class RefreshTokenRequired(BooklyException):
    """User has provided an access token when a refresh token is needed"""
    pass
class UserAlreadyExists(BooklyException):
    """User has provided an email for a user who exists during sign up"""
    pass 

class InvalidCreadentials(BooklyException):
    """User has provided wrong email or password  during log in"""
    pass

class InsufficientPermission(BooklyException):
    """User does not have the neccessary permissions to perform an action"""
    pass

class BookNotFound(BooklyException):
    """Book Not Found"""
    pass

class UserNotFound(BooklyException):
    """User Not Found"""
    pass

def create_exception_handler(status_code:int,initial_detail:Any) ->Callable[[Request,Exception],JSONResponse]:
    pass