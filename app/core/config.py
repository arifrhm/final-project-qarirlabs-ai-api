from pydantic import BaseSettings


class Settings(BaseSettings):
    ROBOFLOW_API_KEY: str
    MODEL_ID: str

    class Config:
        env_file = ".env"


settings = Settings()
