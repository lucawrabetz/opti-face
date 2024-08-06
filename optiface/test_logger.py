import logging
import logging.config

from optiface import ui

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_logging():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")
    ui.header("This is a header")
    ui.subheader("This is a subheader")
    ui.special("This is a special message")
    ui.body("This is a body message")


if __name__ == "__main__":
    test_logging()
