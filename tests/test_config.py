import pytest
from dataclasses import FrozenInstanceError

from src.config import BASE_DIR, load_config, Config, BotConfig


def test_load_config() -> None:
    config = Config(
        bot=BotConfig(
            token="example",
        ),
    )

    loaded_config = load_config(BASE_DIR / "tests" / "example.env")

    assert config == loaded_config


@pytest.mark.parametrize("config, field", [
    (Config(bot=BotConfig(token="123")), "bot"),
    (BotConfig(token="123"), "token"),
])
def test_config_frozen(config: Config | BotConfig, field: str) -> None:
    with pytest.raises(FrozenInstanceError):
        setattr(config, field, "incorrect")
