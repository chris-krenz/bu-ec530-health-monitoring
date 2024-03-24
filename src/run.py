"""

"""

import logging as log

from utils import logger
from utils import id


def main():

    logger.config_logger()

    test = id.LastFirstMiddleName('Doe', 'John', '')
    log.info(test)


if __name__ == '__main__':
    main()
