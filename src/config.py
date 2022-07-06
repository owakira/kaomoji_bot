import pathlib
from dataclasses import dataclass

from environs import Env

BASE_DIR = pathlib.Path(__file__).parent.parent


@dataclass(frozen=True)
class BotConfig:
    """Dataclass that stores bot configs"""

    token: str


@dataclass(frozen=True)
class Config:
    """Dataclass that stores all configs"""

    bot: BotConfig


def load_config(path_to_dotenv_file: str | pathlib.Path = None) -> Config:
    """
    Loads data from dotenv file and make Config with this data
    :param path_to_dotenv_file: Path to a dotenv file
    :type path_to_dotenv_file: str | pathlib.Path
    :return: Made config
    :rtype: Config
    """
    env = Env()
    env.read_env(path_to_dotenv_file)

    return Config(
        bot=BotConfig(
            token=env.str("BOT_TOKEN"),
        ),
    )
