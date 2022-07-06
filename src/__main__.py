import logging

from aiogram import Bot, Dispatcher

from src.config import load_config, BASE_DIR
from src.core.events import on_shutdown, on_startup
from src.core.logging import configure_logging

logger = logging.getLogger(__name__)


def register_middlewares(dp: Dispatcher) -> None:
    pass


def register_routers(dp: Dispatcher) -> None:
    pass


def register_filters(dp: Dispatcher) -> None:
    pass


def main() -> None:
    config = load_config(BASE_DIR / ".env")
    configure_logging(BASE_DIR / "log_config.yml")

    bot = Bot(config.bot.token, parse_mode="HTML")

    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    register_middlewares(dp)
    register_filters(dp)
    register_routers(dp)

    dp.run_polling(bot)


if __name__ == "__main__":
    main()
