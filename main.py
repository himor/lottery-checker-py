import logging
import logging.config
import datetime
import sys

logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)
logger.warning("hello " + datetime.datetime.today().__str__())