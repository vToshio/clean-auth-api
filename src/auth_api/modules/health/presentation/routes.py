from fastapi import APIRouter, Depends
from typing import Annotated

from .docs import router_docs, healthcheck_docs
from .schemas import HealthStatusResponse
from ..application.use_cases import HealthStatusUseCases
from ..infrastructure.dependencies import get_health_check_use_case

router = APIRouter(**router_docs)

@router.get('/healthcheck', **healthcheck_docs)
async def healthcheck_status(
    use_case: Annotated[
        HealthStatusUseCases,
        Depends(get_health_check_use_case)
    ]
) -> HealthStatusResponse:
    response = await use_case.check()
    return HealthStatusResponse(status=response.status)
