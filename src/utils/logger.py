import logging
from src.utils.generate_config import app_config


class Logger:

    def __init__(self):

        self._log_name = app_config["APP_NAME"]
        self._log_dir = app_config["LOG_DIR"]

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        self.__debug_log = logging.getLogger(self._log_name + "_debug")
        self.__debug_log.setLevel(logging.DEBUG)
        debug_handler = logging.FileHandler(self._log_dir + "/" + self._log_name + "_debug.log")
        debug_handler.setFormatter(formatter)
        self.__debug_log.addHandler(debug_handler)
        self.debug = self.__debug_log.debug

        self.__info_log = logging.getLogger(self._log_name + "_info")
        self.__info_log.setLevel(logging.INFO)
        info_handler = logging.FileHandler(self._log_dir + "/" + self._log_name + "_info.log")
        info_handler.setFormatter(formatter)
        self.__info_log.addHandler(info_handler)
        self.info = self.__info_log.info

        self.__error_log = logging.getLogger(self._log_name + "_error")
        self.__error_log.setLevel(logging.ERROR)
        error_handler = logging.FileHandler(self._log_dir + "/" + self._log_name + "_error.log")
        error_handler.setFormatter(formatter)
        self.__error_log.addHandler(error_handler)
        self.error = self.__error_log.error
