from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE_PATH = str(Path(__file__).resolve().parent.parent / ".env")


class Settings(BaseSettings):

    APP_NAME: str = "tg_bot"
    TG_TOKEN: str
    BACKEND_HOST: str
    API_VERSION: str

    @property
    def BACKEND_API(self) -> str:
        return f"{self.BACKEND_HOST}{self.API_VERSION}"

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, env_file_encoding="utf-8")


settings = Settings()
