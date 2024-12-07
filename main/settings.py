from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE_PATH = str(Path(__file__).resolve().parent.parent / ".env")


class Settings(BaseSettings):

    APP_NAME: str = "tg_bot"
    TG_TOKEN: str

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, env_file_encoding="utf-8")


settings = Settings()
