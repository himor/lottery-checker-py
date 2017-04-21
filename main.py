import logging
import logging.config
import datetime
import lottery
import rangea
import freqa
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

ra = rangea.RangeAnalyser()
ra.analyse(lottery.data)
print(ra.check([1,2,69,70,71]))