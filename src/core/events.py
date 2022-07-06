import logging

logger = logging.getLogger(__name__)


async def on_startup() -> None:
    logger.info("Starting bot!")


async def on_shutdown() -> None:
    logger.error("Bot has been stopped!")
