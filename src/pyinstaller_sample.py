import logging
import logging.config
import time

import yaml

from child import child

with open("./configs/log_conf.yml") as f:
    logging.config.dictConfig(yaml.unsafe_load(f.read()))

logger = logging.getLogger(__name__)


def main():
    logger.info("PyInstaller sample start.")
    for i in range(5):
        logger.info("Runnning...")
        child.exec()
        time.sleep(1)
    logger.info("PyInstaller sample end.")


if __name__ == "__main__":
    main()
