import random

# Thin wrapper for mockability
class Randomizer(object):
    def __init__(self):
        super(Randomizer, self).__init__()

    def chooseRandomIndex(self, i):
        return random.randint(0, i - 1)

    def shuffle(self, array):
        random.shuffle(array)
        return array