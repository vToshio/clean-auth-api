from ..application.use_cases import HealthStatusUseCases

def get_health_check_use_case() -> HealthStatusUseCases:
    return HealthStatusUseCases()
