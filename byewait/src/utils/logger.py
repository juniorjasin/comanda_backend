import logging


class Logger():
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(message)

    def info(self, message):
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def warning(self, message):
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(message)

    def error(self, message):
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message)
    
    def critical(self, message):
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical(message)