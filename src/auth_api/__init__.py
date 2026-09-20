from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from .shared.infrastructure.settings import settings
from .shared.infrastructure.resources import lifespan
from .shared.presentation.routes import routers
from .shared.presentation.handlers import http_exception_handler, internal_exception_handler

app = FastAPI(
    debug=settings.debug,
    title=settings.api_title,
    summary=settings.api_summary,
    version=settings.api_version,
    docs_url='/',
    lifespan=lifespan,
)

for router in routers:
    app.include_router(router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, internal_exception_handler)