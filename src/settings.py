from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic.fields import computed_field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    ACCESS_TOKEN_SECRET_KEY: str
    REFRESH_TOKEN_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRES_MINUTES: int
    REFRESH_TOKEN_EXPIRES_MINUTES: int
    ALGORITHM: str = "HS256"
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    DB_USER_HOST: str
    DB_USER_USER: str
    DB_USER_PWD: str
    DB_USER_PORT: int
    DB_USER_DEFAULTDB: str
    DB_DATA_HOST: str
    DB_DATA_USER: str
    DB_DATA_PWD: str
    DB_DATA_PORT: int
    DB_DATA_DEFAULTDB: str

    @computed_field
    @property
    def DB_DATA_URL(self) -> str:
        return f'clickhouse+asynch://{self.DB_DATA_USER}:{self.DB_DATA_PWD}@{self.DB_DATA_HOST}:{self.DB_DATA_PORT}/{self.DB_DATA_DEFAULTDB}'

    @computed_field
    @property
    def DB_USER_URL(self) -> str:
        return f'clickhouse+asynch://{self.DB_DATA_USER}:{self.DB_DATA_PWD}@{self.DB_DATA_HOST}:{self.DB_DATA_PORT}/{self.DB_DATA_DEFAULTDB}'


settings = Settings()
