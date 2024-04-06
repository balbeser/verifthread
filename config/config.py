from dataclasses import dataclass
from environs import Env


@dataclass
class PostgreSQL:
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    NAME: str


@dataclass
class BotSettings:
    token: str


@dataclass
class Config:
    Bot: BotSettings
    DataBase: PostgreSQL


def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        Bot=BotSettings(token=env("BOT-TOKEN")),
        DataBase=PostgreSQL(
            USER=env("DB-USER"),
            PASSWORD=env("DB-PASSWORD"),
            HOST=env("DB-HOST"),
            PORT=env("DB-PORT"),
            NAME=env("DB-NAME"),
        ),
    )
