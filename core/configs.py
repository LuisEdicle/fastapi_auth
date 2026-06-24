from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_VI_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://geek:university@localhsot:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_secret: str = 'IswNyG7DN6LruZ7rpxYllSZR2EEgAiLCSCtleA0UyEw'

    """
    import secrets
    token: str = secrets.token_urlsafe(32)

    """
    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()