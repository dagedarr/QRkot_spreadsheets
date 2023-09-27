from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд'
    description: str = 'Сервис для поддержки котиков!'
    secret: str = 'SECRET'

    database_url: str = 'sqlite+aiosqlite:///./sqlite_db.db'

    class Config:
        env_file = '.env'


settings = Settings()