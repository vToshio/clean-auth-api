from dataclasses import dataclass
from ..domain.enums import HealthStatusEnum
from ....shared.domain.exceptions import StandardException, ServerException

@dataclass
class HealthCheckOutput:
    status: HealthStatusEnum

class HealthStatusUseCases:
    async def check(self) -> HealthCheckOutput:
        try:
            return HealthCheckOutput(
                status=HealthStatusEnum.OK
            )
        except StandardException:
            raise
        except Exception as e:
            raise ServerException()