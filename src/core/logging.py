import logging
import logging.config
import pathlib

import yaml


class ColoredFormatter(logging.Formatter):
    """Formatter that shows logs in color"""
    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record: logging.LogRecord):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def configure_logging(path_to_log_config_file: str | pathlib.Path) -> dict:
    """
     Loads log config from yaml file.
     And configures logging using logging.config.dictConfig
     :param path_to_log_config_file: path to log yaml file
     :type path_to_log_config_file: str | pathlib.Path
     :return: Loaded config
     :rtype: dict
     """
    with open(path_to_log_config_file, "r") as stream:
        data = yaml.load(stream, yaml.FullLoader)
    logging.config.dictConfig(data)

    return data
