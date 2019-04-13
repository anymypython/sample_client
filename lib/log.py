import logging
from config import settings


class Logger:
    """
    日志助手
    """

    def __init__(self):
        self.path = settings.LOG_FILE_PATH
        file_handler = logging.FileHandler(self.path, "a", encoding="utf-8")
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        file_handler.setFormatter(fmt)
        self.logger = logging.Logger("cmdb", level=logging.INFO)
        self.logger.addHandler(file_handerler)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)


logger = Logger()
