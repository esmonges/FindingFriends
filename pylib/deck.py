class Deck(object):
    """Object representing a deck that can contain any multiple of 54 cards"""
    def __init__(self, cardsets):
        super(Deck, self).__init__()
        assert (cardsets >= 1)
        self.cardsets = cardsets
        


