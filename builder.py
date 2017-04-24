import random

class Builder(object):
    def populate(self):
        numbers = [i for i in range(1, 76)]
        random.shuffle(numbers)
        numbers = numbers[:5]
        numbers.sort()
        self.numbers = numbers
        self.megaball = random.randrange(1, 16)

    def get_numbers_string(self):
        return " ".join(map(str, self.numbers)) + " " + str(self.megaball)
