import pathlib
from dataclasses import dataclass

from environs import Env

BASE_DIR = pathlib.Path(__file__).parent.parent


@dataclass(frozen=True)
class BotConfig:
    """Dataclass that store bot configs."""

    token: str


@dataclass(frozen=True)
class Config:
    bot: BotConfig


def load_config(path_to_dotenv_file: str | pathlib.Path = None) -> Config:
    env = Env()
    env.read_env(path_to_dotenv_file)

    return Config(
        bot=BotConfig(
            token=env.str("BOT_TOKEN"),
        ),
    )
