import os
import logging
import logging.config

from src.config.consts import LOGINI_PATH


def getLogger(logger_name: str):
    """loggerを取得する.

    Args:
        logger_name (str): log.iniに書いてあるloggerの中から一つ選ぶ.
    """
    logging.config.fileConfig(LOGINI_PATH)
    logger = logging.getLogger(logger_name)

    return logger
