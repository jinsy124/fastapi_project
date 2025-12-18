from typing import Any,Callable
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi import status


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
    async def exception_handler(request:Request,exc:BooklyException):
        return JSONResponse(
            content=initial_detail,
            status_code=status_code
        )
    return exception_handler

def register_all_errors(app:FastAPI):
    app.add_exception_handler(
        UserAlreadyExists,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message":"User with email already exists",
                "error_code":"user_exists"
            }
        )
    )
    app.add_exception_handler(
        AccessTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_detail={
                "message":"please provide a valid access token",
                "resolution":"please get an access token",
                "error_code":"access_token_required"

            
            }
        )
    )
    app.add_exception_handler(
        RefreshTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message":"please provide a valid refresh token",
                "resolution":"please get an refresh token",
                "error_code":"refresh token required"
            }
        )
    )

    app.add_exception_handler(
        InsufficientPermission,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message": "You do not have permission to perform this action",
                "resolution": "Contact the administrator for access",
                "error_code": "insufficient_permission",
            },
        ),
    )
    app.add_exception_handler(
        InvalidToken,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_detail={
                "message":"Token is invalid or expired",
                "error_code":"invalid_token"
            }
        )
    )
    app.add_exception_handler(
        RevokedToken,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_detail={
                "message":"Token is invalid or has been revoked",
                "error_code":"token_revoked"
            }
        )
    )
    app.add_exception_handler(
        InvalidCreadentials,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_detail={
                "message": "Invalid email or password",
                "resolution": "Check your credentials and try again",
                "error_code": "invalid_credentials",
            },
        ),
    )
    app.add_exception_handler(
        UserNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message": "User not found",
                "resolution": "Verify the user ID and try again",
                "error_code": "user_not_found",
            },
        ),
    )
    app.add_exception_handler(
        BookNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message": "Book not found",
                "resolution": "Verify the book ID and try again",
                "error_code": "book_not_found",
            },
        ),
    )


async def internal_server_error(request,exc):

        return JSONResponse(
            content={
                "message":"Oops something went wrong","error_code":"server_error"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
         )

