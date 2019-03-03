from pylib.Game.Modules.Randomizer import Randomizer

class Fake_Randomizer(Randomizer):
    def __init__(self):
        super(Fake_Randomizer, self).__init__()

    def chooseRandomIndex(self, i):
        return i - 1 # TODO: Does python have interface support for this?

    def shuffle(self, array):
        array.reverse()
        return array