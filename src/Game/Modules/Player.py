import bisect
import uuid
from src.Game.Modules.Card import Card


class Player(object):
    def __init__(self, name=str(), hand=list()):
        """
        Player - constructor

        A player has a name and a hand of cards. Constructs the player object
        based on their name and a list of cards (defaults to empty list)

        :param name: string that is the name of the player
        :param hand: Optional; list of Card objects. Defaults to []
        """
        super(Player, self).__init__()
        self.display_name = name
        self.user_uuid = str(uuid.uuid4())
        self.hand = hand

    def set_hand(self, hand=list):
        self.hand = hand

    def __repr__(self):
        """
        Python representation for this Player
        :return:
        """
        return "Player(%r, %r)" % (self.display_name, self.hand)

    def __str__(self):
        """
        String representing the player
        :return:
        """
        return "%r %r" % (self.display_name, str(self.hand))

    def __eq__(self, other):
        """
        :type other: Player
        """
        try:
            return self.get_info() == other.get_info()
        except AttributeError:
            return False

    def get_info(self):
        """
        Info given is the name of the player and the uuid
        :return:
        """
        return self.display_name, self.user_uuid

    def add_card_to_hand(self, card: Card):
        """
        Method to stick a card into a player's hand
        inserts card into self.hand in a sorted manner
        :param card: Card object to put into the hand
        :return:
        """
        bisect.insort(self.hand, card)

    def get_hand(self):
        """
        The hand of the player
        :return: array of cards
        """
        return self.hand

