from fastapi import FastAPI ,status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from src.reviews.routes import review_router
from src.books.routes import book_router
from src.auth.routers import auth_router   # ✅ ADD THIS

from .errors import register_all_errors
from .middleware import register_middleware




version = "v1"

app = FastAPI(
    title="Bookly",
    description="A Rest API for a book review web service",
    version=version,
   
    
)

register_all_errors(app)

register_middleware(app)



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

