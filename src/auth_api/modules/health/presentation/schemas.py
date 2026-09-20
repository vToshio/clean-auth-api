from pydantic import BaseModel, Field
from ..domain.enums import HealthStatusEnum

class HealthStatusResponse(BaseModel):
    status: HealthStatusEnum = Field(
        title='Health status',
        description='Brief disponibility description based on the current API health.',
        examples=['ok', 'error']
    )