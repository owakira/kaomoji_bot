from dataclasses import FrozenInstanceError

import pytest

from src.config import BASE_DIR, BotConfig, Config, load_config


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
