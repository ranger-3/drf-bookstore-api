from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    secret_key: SecretStr

    db_name: str
    db_user: str
    db_password: SecretStr
    db_host: str
    db_port: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
