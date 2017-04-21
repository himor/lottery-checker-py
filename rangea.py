
class RangeAnalyser(object):

    def analyse(self, data):
        result = [{'min': 76, 'max':0} for __ in range(0,6)]
        for item in data:
            for p, num in enumerate(item['numbers']):
                if result[p+1]['min'] > num:
                    result[p+1]['min'] = num
                if result[p+1]['max'] < num:
                    result[p+1]['max'] = num
        self.cache = result

    def check(self, set):
        normal = []
        for p, num in enumerate(set):
            p += 1
            if self.cache[p]['min'] > num or self.cache[p]['max'] < num:
                normal.append(p-1)
        return normal