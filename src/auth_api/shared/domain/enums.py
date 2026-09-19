from enum import StrEnum

class ApplicationEnvironment(StrEnum):
    PROD = 'production'
    HOMOLOG = 'staging'
    DEV = 'development'
