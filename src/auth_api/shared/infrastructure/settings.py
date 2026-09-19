from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator
from functools import lru_cache

from ..domain.enums import ApplicationEnvironment

class Settings(BaseSettings):
    api_title: str = 'Auth-API'
    api_summary: str = ''
    api_version: str = '0.0.0'
    environment: ApplicationEnvironment = ApplicationEnvironment.DEV
    debug: bool = True  

    @model_validator(mode='after')
    def normalize_debug(self):
        self.debug = self.environment != ApplicationEnvironment.PROD
        return self 

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()