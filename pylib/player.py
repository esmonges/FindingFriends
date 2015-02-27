class Player(object):
    """class representing a Player in the game"""
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.hand = []

    def __repr__(self):
        return "Player(%r)" % (self.name)

    def __str__(self):
        return "%r %r" % (self.name, str(self.hand))

    def insertCard(self, card):
        return


