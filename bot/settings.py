from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    telegram_key: str = ""
    api_base_url: str = "http://api:8080"
    request_timeout_seconds: float = 120.0


settings = Settings()
