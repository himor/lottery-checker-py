
class FrequencyAnalyser(object):

    def analyse(self, data):
        numbers = [[0 for __ in range(0, 76)] for __ in range(0, 6)]
        mballs = [0 for __ in range(0, 16)]

        for item in data:
            for pos, num in enumerate(item['numbers']):
                numbers[pos+1][num] += 1
            mballs[item['mega']] += 1

        maximum = float(len(data))
        for i, j in enumerate(numbers):
            for pos in range(0, len(j)):
                numbers[i][pos] /= maximum * 100.0

        for i in range(0, len(mballs)):
            mballs[i] /= maximum * 100.0

        self.cache = {'numbers': numbers, 'mb': mballs}

    def check(self, set):
        normal = []
        for pos, number in enumerate(set):
            pos += 1
            tempset = self.cache['numbers'][pos]
            right = float(tempset[number])
            for qq in tempset:
                if qq > right:
                    normal.append(pos - 1)

        return normal
