"""
Configuration management for Sentinex Social Intelligence.
Loads settings from environment variables using pydantic-settings.
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application Settings
    app_name: str = "Sentinex Social Intelligence API"
    app_version: str = "0.2.0"
    debug: bool = False
    
    # Database Settings
    database_url: str = Field(
        default="sqlite:///./sentinex.db",
        description="Database connection URL"
    )
    
    # API Keys (Optional - for future phases)
    reddit_client_id: Optional[str] = None
    reddit_client_secret: Optional[str] = None
    reddit_user_agent: Optional[str] = "Sentinex/0.1"
    
    # Data Generation Settings
    synthetic_data_seed: int = 42
    max_synthetic_posts: int = 1000
    
    # Network Analysis Settings
    influence_threshold: float = 0.5
    max_network_nodes: int = 10000
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()
