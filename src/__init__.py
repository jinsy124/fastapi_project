from fastapi import FastAPI ,status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from src.reviews.routes import review_router
from src.books.routes import book_router
from src.auth.routers import auth_router   # ✅ ADD THIS
from src.db.main import init_db
from .errors import(
    create_exception_handler,
    InvalidCreadentials,
    BookNotFound,
    UserAlreadyExists,
    UserNotFound,
    InsufficientPermission,
    AccessTokenRequired,
    InvalidToken,
    RefreshTokenRequired,
    RevokedToken
)

@asynccontextmanager
async def life_span(app: FastAPI):
    print("server is starting.......")
    await init_db()
    yield
    print("server has been stopped...")


version = "v1"

app = FastAPI(
    title="Bookly",
    description="A Rest API for a book review web service",
    version=version,
    
)
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

@app.exception_handler(500)
async def internal_server_error(request,exc):

        return JSONResponse(
            content={
                "message":"Oops something went wrong","error_code":"server_error"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
         )



# Books routes
app.include_router(
    book_router,
    prefix=f"/api/{version}/books",
    tags=["books"]
)

# Auth routes ✅ THIS WAS MISSING
app.include_router(
    auth_router,
    prefix=f"/api/{version}/auth",
    tags=["auth"]
)
app.include_router(
    review_router,
    prefix=f"/api/{version}/reviews",
    tags=["reviews"]
)

