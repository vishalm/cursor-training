import os
from pathlib import Path
from typing import List, Optional
import yaml
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Server settings
    FLASK_APP: str = "run.py"
    FLASK_ENV: str = "development"
    FLASK_DEBUG: bool = True
    
    # API settings
    API_VERSION: str = "v1"
    API_PREFIX: str = "/api"
    
    # Ollama settings
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen2.5:latest"
    OLLAMA_TEMPERATURE: float = 0.7
    OLLAMA_MAX_TOKENS: int = 1000
    OLLAMA_TIMEOUT: int = 30
    
    # Storage settings
    STORAGE_TYPE: str = "memory"
    STORAGE_CLEANUP_INTERVAL: int = 3600  # 1 hour
    MAX_CART_ITEMS: int = 50
    MAX_CONVERSATION_AGE: int = 86400  # 24 hours
    
    # Security settings
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY: int = 3600  # 1 hour
    PASSWORD_SALT: str
    
    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    
    # CORS settings
    CORS_ORIGINS: List[str] = ["*"]
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "allow"  # Allow extra fields from environment variables
    }

def load_config() -> Settings:
    """Load configuration from config.yaml and environment variables."""
    config_path = Path(__file__).parent.parent.parent / "config.yaml"
    
    if config_path.exists():
        with open(config_path) as f:
            config_data = yaml.safe_load(f)
            
            # Flatten nested configuration and update environment variables
            for section, values in config_data.items():
                if isinstance(values, dict):
                    for key, value in values.items():
                        env_key = f"{section.upper()}_{key.upper()}"
                        os.environ[env_key] = str(value)
                else:
                    os.environ[section.upper()] = str(values)
    
    return Settings()

settings = load_config() 