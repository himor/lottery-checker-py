
class RangeAnalyser(object):

    def analyse(self, data):
        result = [{'min': 76, 'max':0} for __ in range(0,6)]
        for item in data:
            for pos, num in enumerate(item['numbers']):
                if result[pos + 1]['min'] > num:
                    result[pos + 1]['min'] = num
                if result[pos + 1]['max'] < num:
                    result[pos + 1]['max'] = num
        self.cache = result

    def check(self, set):
        normal = []
        for pos, num in enumerate(set):
            pos += 1
            if self.cache[pos]['min'] > num or self.cache[pos]['max'] < num:
                normal.append(pos - 1)
        return normal
