import datetime
"""
experinmenting with logger
"""
class Logger(object):
    TYPE_SCREEN = 1
    TYPE_FILE   = 2

    type = TYPE_SCREEN
    prefix = ""

    def __init__(self, filename):
        self.filename = filename

    def setType(self, type):
        if type == self.TYPE_SCREEN:
            self.type = self.TYPE_SCREEN
            return
        if type == self.TYPE_FILE:
            self.type = self.TYPE_FILE
            return
        if type == self.TYPE_FILE + self.TYPE_SCREEN:
            self.type = self.TYPE_FILE + self.TYPE_SCREEN
            return

    def setPrefix(self, prefix):
        self.prefix = prefix

    def log(self, message):
        micro = int(datetime.datetime.now().__format__("%f")) / 100
        prefix = '[{}.{}]'.format(datetime.datetime.now().__format__("%Y-%m-%d %H:%M:%S"), micro)
        prefix = prefix + self.prefix
        if self.type & self.TYPE_SCREEN:
            print prefix + message
        if self.type & self.TYPE_FILE:
            with open(self.filename, "a+") as logfile:
                try:
                    logfile.write(prefix + message + "\n")
                finally:
                    logfile.close()

