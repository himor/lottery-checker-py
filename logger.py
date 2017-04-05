import datetime
class Logger:
    TYPE_SCREEN = 1
    TYPE_FILE   = 2

    filename = ""
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
        prefix = "[" + datetime.datetime.now().__format__("%Y-%m-%d %H:%M:%S.") + str(micro) + "] "
        prefix = prefix + self.prefix
        if self.type & self.TYPE_SCREEN:
            print prefix + message
        if self.type & self.TYPE_FILE:
            f = open (self.filename, "a+")
            f.write(prefix + message + "\n")

