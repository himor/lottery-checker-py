class DistanceAnalyser(object):

    def analyse(self, data):
        pass

    def check(self, set):
        pass

da = DistanceAnalyser()
da.analyse([
    {'numbers':[1, 10, 20, 30, 55], 'mega':5},
    {'numbers':[1, 20, 30, 40, 60], 'mega':14},
    {'numbers':[10, 20, 30, 40, 60], 'mega':3}
    ])

res = da.check([1, 20, 30, 40, 60])
print(res)