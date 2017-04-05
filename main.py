import logger, datetime

log = logger.Logger("log.txt")
log.setType(log.TYPE_FILE + log.TYPE_SCREEN)
log.log("hello " + datetime.datetime.today().__str__())

