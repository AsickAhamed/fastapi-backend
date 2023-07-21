from src.utils.generate_config import app_config
from src.utils.logger import Logger
if __name__ == "__main__":
    log_helper = Logger()
    log_helper.debug("application started")
    log_helper.info("log from info")
    log_helper.error("log from error")
    print("hello world")
    print(app_config["HOST"])
    print(app_config["DB"])

