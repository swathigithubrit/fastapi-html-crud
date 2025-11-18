from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_tables_database
from app.routers import user_routes
from fastapi.staticfiles import StaticFiles


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables_database()
    yield

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory = "app/static"), name = "static")

app.include_router(user_routes.router)

