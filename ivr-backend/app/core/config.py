"""Configuration management using Pydantic Settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DATABASE_URL: str = Field(
        description="PostgreSQL database connection URL",
    )
    REDIS_URL: str = Field(
        description="Redis connection URL",
    )
    API_KEY: str = Field(
        description="API key for dashboard authentication",
    )
    APP_ENV: str = Field(
        default="development",
        description="Application environment",
    )
    LOG_LEVEL: str = Field(
        default="debug",
        description="Logging level",
    )


settings = Settings()
