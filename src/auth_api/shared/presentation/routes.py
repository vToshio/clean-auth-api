from fastapi import APIRouter
from typing import List

# set your routers imports here
from auth_api.modules.health.presentation.routes import router as health_router

# Set your routers here
routers: List[APIRouter] = [
    health_router
]