import logging


class logger:

    def __init__(self):
        self.logger = logging.getLogger("watchbird")
        self.handler = logging.FileHandler("logs/watchbird.log")
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

        self.error_logger = logging.getLogger("watchbird_error")
        self.error_handler = logging.FileHandler("logs/watchbird_error.log")
        self.error_handler.setFormatter(self.formatter)
        self.error_logger.addHandler(self.error_handler)

