import logging
import logging.config
import datetime
import lottery
from bcolors import bcolors

# setting up logging
logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)
logger.info("Start {}".format(datetime.datetime.today()))

# fetch lottery data
lottery = lottery.Lottery()
lottery.fetch()
logger.info("Fetched {} sets".format(len(lottery.data)))

for i in range (0,5):
    print(bcolors.OKBLUE + lottery.data[i]['date'] + bcolors.ENDC + " {num} ({mega})".format(
        num = " ".join(map(str, lottery.data[i]['numbers'])),
        mega = lottery.data[i]['mega'],
        ))