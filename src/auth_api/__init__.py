from fastapi import FastAPI

from .shared.domain.enums import ApplicationEnvironment
from .shared.infrastructure.settings import settings
from .shared.infrastructure.resources import lifespan
from .shared.presentation.routes import routers

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

