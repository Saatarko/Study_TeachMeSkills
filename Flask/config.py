import os

# from pydantic_settings import BaseSettings, SettingsConfigDict
#
#
# class Settings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME: str
#
#     @property
#     def database_url_psycopg(self):
#         # DSN
#         # postgresql+psycopg://postgres:postgres@localhost:5432/sa
#         return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
#
#     model_config = SettingsConfigDict(env_file=".env")

#
# settings = Settings()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'rfr;tdsvtyzpft,fkb'
