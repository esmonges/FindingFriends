from src.Game.Modules.Card import Card
from src.Game.Modules import CardConstants
from src.Game.Modules.Deck import Deck
from src.Game.Modules.Player import Player
from src.Game.Modules.Randomizer import Randomizer
from math import ceil


class Round(object):
    players = False  # type: List[Player]
    firstDrawPlayerIndex = 0  # type: int
    currentDrawPlayerIndex = 0  # type: int
    currentAlphaPlayerIndex = False  # type: int
    currentTrumpSuitDeclaringPlayerIndex = False  # type: int
    previousTrumpSuitDeclaringPlayerIndex = False  # type: int
    randomizer = False  # type: Randomizer
    trumpNumber = 0  # type: int
    trumpSuit = False  # type: str
    trumpSuitDeclarationLength = 0  # type: int
    deck = False  # type: Deck
    previouslyDeclaredSetByPlayer = False

    NOT_TRUMP_NUMBER_ERROR = 'Cards used to declare trump suit are not of trump number'
    TRUMP_DECLARATION_MISMATCH_ERROR = 'Cards used to declare trump suit do not all match'
    INVALID_PLAYER_ERROR = 'Player not in game given'
    PLAYER_MISSING_CARDS_FOR_CALL_ERROR = 'Player does not have cards to call trump suit'
    MORE_IF_PREVIOUSLY_DECLARED_ERROR = 'Must declare with at least as many cards as were previously declared'
    MORE_TO_REDECLARE_ERROR = 'Must declare with more cards if you are not a player that has previously declared'


    def __init__(self, players=False, randomizer=False, trumpNumber=0):
        super(Round, self).__init__()
        if not players:
            players = []
        if not randomizer:
            randomizer = Randomizer()
        if not trumpNumber:
            trumpNumber = CardConstants.NUMBERS[0]

        self.players = players
        self.randomizer = randomizer
        self.trumpNumber = trumpNumber
        self.previouslyDeclaredSetByPlayer = {}

    def determineStartDrawPlayer(self):
        self.firstDrawPlayerIndex = self.randomizer.chooseRandomIndex(len(self.players))

    def initializeDeck(self):
        self.deck = Deck(randomizer=self.randomizer, cardsets=int(ceil(len(self.players)/2.0)))
        self.deck.generateDeck()

    def shuffleDeck(self):
        self.deck.shuffleDeck()

    def drawFromDeckForCurrentPlayer(self):
        self.players[self.currentDrawPlayerIndex].add_card_to_hand(self.deck.draw())
        self.currentDrawPlayerIndex = (self.currentDrawPlayerIndex + 1) % len(self.players)

    def declareTrumpSuitByPlayer(self, player, cards):
        """

        :type cards: List[Card]
        :type player: Player
        """
        # Validate that the cards we're using to jump are valid
        self.validateTrumpCallCards(cards)

        playerCallingIndex = self.findPlayerIndex(player)
        # Validate that we have more cards than the current declaration
        self.validateRedeclaration(player, cards)

        playerDoesHaveCardsUsedToCall = self.playerDoesHaveCardsToCallTrumpSuit(playerCallingIndex, cards)
        if playerDoesHaveCardsUsedToCall:
            if self.currentAlphaPlayerIndex is False:
                self.currentAlphaPlayerIndex = playerCallingIndex
            self.previouslyDeclaredSetByPlayer[player.get_info()] = cards
            self.trumpSuit = cards[0].suit
            self.trumpSuitDeclarationLength = len(cards)
        else:
            raise ValueError(self.PLAYER_MISSING_CARDS_FOR_CALL_ERROR)

    def validateRedeclaration(self, callingPlayer, cards):
        """
        If player calling called previously AND used the same suit, they must have geq the current call length
        Otherwise, they must have strictly greater than the current call length

        :type callingPlayer: Player
        :type cards: List[Card]
        """
        if callingPlayer.get_info() in self.previouslyDeclaredSetByPlayer.keys()\
                and self.previouslyDeclaredSetByPlayer[callingPlayer.getIdentifier()][0].suit == cards[0].suit:
            if len(cards) < self.trumpSuitDeclarationLength:
                raise ValueError(self.MORE_IF_PREVIOUSLY_DECLARED_ERROR)
        else:
            if len(cards) <= self.trumpSuitDeclarationLength:
                raise ValueError(self.MORE_TO_REDECLARE_ERROR)


    def validateTrumpCallCards(self, cards):
        firstCard = cards[0]
        if firstCard.number != self.trumpNumber:
            raise ValueError(self.NOT_TRUMP_NUMBER_ERROR)
        for card in cards:
            if card != firstCard:
                raise ValueError(self.TRUMP_DECLARATION_MISMATCH_ERROR)

    def findPlayerIndex(self, player):
        for i, gamePlayer in enumerate(self.players):
            if gamePlayer == player:
                return i

        raise ValueError(self.INVALID_PLAYER_ERROR)

    def playerDoesHaveCardsToCallTrumpSuit(self, playerIndex, cards):
        cardsIndex = 0
        foundCards = 0
        for card in self.players[playerIndex].hand:
            if card == cards[cardsIndex]:
                foundCards += 1
                cardsIndex += 1
            if foundCards == len(cards):
                return True
        return False
