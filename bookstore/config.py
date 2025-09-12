from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: SecretStr

    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
