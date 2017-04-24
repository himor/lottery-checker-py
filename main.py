import logging
import logging.config
import datetime
import lottery
import rangea
import freqa
import builder
from bcolors import bcolors

# setting up logging
logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)
logger.info("Start {}".format(datetime.datetime.today()))

# fetch lottery data
lottery = lottery.Lottery()
lottery.fetch()
logger.info("Fetched {} sets".format(len(lottery.data)))

# display fetched data
freq = freqa.FrequencyAnalyser()
freqRes = freq.analyse(lottery.data)

for i in range (0,5):
    print("{}\t".format(lottery.data[i]['date'])),
    err = freq.check(lottery.data[i]['numbers'])

    if len(err) > 0:
        print(bcolors.FAIL + "freq: fail" + bcolors.ENDC)
    else:
        print(bcolors.OKGREEN + "freq: pass" + bcolors.ENDC)

    for pos, value in enumerate(lottery.data[i]['numbers']):
        if pos in err:
            print(bcolors.FAIL + "{}\t".format(value) + bcolors.ENDC),
        else:
            print(bcolors.OKGREEN + "{}\t".format(value) + bcolors.ENDC),
        
        for k in range(1, 6):
            print("%.3f\t" % freqRes['numbers'][value][k]),

        print

    print("mega %2d (%.2f)\n" % (lottery.data[i]['mega'], freqRes['mb'][lottery.data[i]['mega']]))

