from fastapi import FastAPI
from fastapi_pagination import Page, add_pagination

from src.apps.user.api import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1/users", tags=["users"])

add_pagination(app)
