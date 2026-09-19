from fastapi import FastAPI
from contextlib import asynccontextmanager

from .settings import settings
from ..domain.enums import ApplicationEnvironment

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await startup(app)
        yield
    finally:
        await shutdown()


async def startup(app: FastAPI):
    try:
        print(f'[SYSTEM] Starting {app.title} life-state...')

        if settings.environment == ApplicationEnvironment.DEV:
            print("Starting your app in DEVELOPMENT MODE. That's not recommended in production.")
    except Exception as e:
        raise

async def shutdown():
    try:
        print('[SYSTEM] Shutting down {settings.api_title}.')
    except Exception as e:
        raise