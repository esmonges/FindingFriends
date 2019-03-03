import unittest
from pylib.Game.Modules.Randomizer import Randomizer
from pylib.Game.Modules.Card import Card
from pylib.Game.Test_Utils.Game_Test_Orchestrator import Game_Test_Orchestrator
from pylib.Game.Test_Utils.Fake_Ranomizer import Fake_Randomizer


class Game_Test(unittest.TestCase):
    def setUp(self):
        # Ted's python learning notes on test framework:
        # setUp DOES get called before each method, not just the class.
        # But Game(player, stuff=[]) results in the default value for stuff being a ref
        # that will persist between constructor calls to Game. Which is silly, but hey.
        self.orchestrator = Game_Test_Orchestrator()
        return

    # make a new game
    def test_it_starts_a_game(self):
        self.orchestrator.startGame()
        assert self.orchestrator.game.players == []

    # add players to the game
    def test_it_registers_players(self):
        self.orchestrator.startGame()
        self.orchestrator.registerPlayers()
        assert self.orchestrator.game.players[0].name == 'Ted'
        assert self.orchestrator.game.players[1].name == 'Mary'
        assert self.orchestrator.game.players[2].name == 'Kevin'
        assert self.orchestrator.game.players[3].name == 'Kathee'

    # start a round
    def test_it_starts_a_round(self):
        self.orchestrator.startGame()
        self.orchestrator.registerPlayers()
        self.orchestrator.startRound()
        assert self.orchestrator.game.players == self.orchestrator.game.currentRound.players
        assert self.orchestrator.game.currentRound.trumpNumber == Card.TWO

    # choose who draws first
    def test_it_chooses_a_random_start_player(self):
        self.orchestrator.startGame(Randomizer())
        self.orchestrator.registerPlayers()
        self.orchestrator.startRound()
        # Random test, do it a bunch to try and ensure determinism
        for i in xrange(1, 30):
            self.orchestrator.determineStartPlayer()
            assert self.orchestrator.game.currentRound.firstDrawPlayerIndex >= 0
            assert self.orchestrator.game.currentRound.firstDrawPlayerIndex < len(self.orchestrator.game.currentRound.players)
            assert isinstance(self.orchestrator.game.currentRound.firstDrawPlayerIndex, int)

    # choose who draws first but deterministically
    def test_it_assigns_a_start_player(self):
        self.orchestrator.startGame(Fake_Randomizer())
        self.orchestrator.registerPlayers()
        self.orchestrator.startRound()
        self.orchestrator.determineStartPlayer()
        assert self.orchestrator.game.currentRound.firstDrawPlayerIndex == 3

    # make a deck to play with based on number of players
    def test_it_generates_a_deck(self):
        self.orchestrator.startGame()
        self.orchestrator.registerPlayers()
        self.orchestrator.startRound()
        self.orchestrator.determineStartPlayer()
        self.orchestrator.initializeRoundDeck()
        deck = self.orchestrator.game.currentRound.deck.deck
        assert len(deck) == 108
        assert deck[0].suit == Card.CLUB
        assert deck[12].suit == Card.CLUB
        assert deck[13].suit == Card.HEART
        assert deck[25].suit == Card.HEART
        assert deck[26].suit == Card.DIAMOND
        assert deck[38].suit == Card.DIAMOND
        assert deck[39].suit == Card.SPADE
        assert deck[51].suit == Card.SPADE

    # shuffle the deck
    def test_it_shuffles_a_deck_randomly(self):
        self.orchestrator.startGame(Randomizer())\
            .registerPlayers()\
            .startRound()\
            .determineStartPlayer()\
            .initializeRoundDeck()\
            .shuffleRoundDeck()

        # TODO: Better way to test non deterministic randomization?
        suitCounts = {}
        deck = self.orchestrator.game.currentRound.deck.deck
        for i in xrange(0, len(deck)):
            if deck[i].suit not in suitCounts.keys():
                suitCounts[deck[i].suit] = 1
            else:
                suitCounts[deck[i].suit] += 1

        for suit in suitCounts:
            if suit == Card.BIG or suit == Card.SMALL:
                assert suitCounts[suit] == 2
            else:
                assert suitCounts[suit] == 26

    # shuffle the deck but deterministically
    # Just reverse for now
    def test_it_shuffles_a_deck_deterministically(self):
        self.orchestrator\
            .startGame(Fake_Randomizer())\
            .registerPlayers()\
            .startRound()\
            .determineStartPlayer()\
            .initializeRoundDeck()\
            .shuffleRoundDeck()

        deck = self.orchestrator.game.currentRound.deck.deck
        assert deck[0].suit == Card.BIG
        assert deck[0].number == Card.JOKER
        assert deck[1].suit == Card.SMALL
        assert deck[1].number == Card.JOKER

    # Have people go around drawing until the deck is empty?
    # make someone declare alpha inside of it?
    def test_pre_game_draw_routine(self):
        self.orchestrator\
            .startGame(Fake_Randomizer())\
            .registerPlayers()\
            .startRound()\
            .determineStartPlayer()\
            .initializeRoundDeck()\
            .shuffleRoundDeck()\
            .simulatePlayersDrawing()

        #TODO Assert more interesting stuff (maybe try to change order of deck a little more
        # Make it so multiple players can jump
        for player in self.orchestrator.game.currentRound.players:
            assert len(player.hand) == 27
        self.assertTrue(self.orchestrator.game.currentRound.currentAlphaPlayerIndex == 2)
        self.assertTrue(self.orchestrator.game.currentRound.trumpSuit)

    def test_simulate_play_first_hand(self):
        self.orchestrator \
            .startGame(Fake_Randomizer()) \
            .registerPlayers() \
            .startRound() \
            .determineStartPlayer() \
            .initializeRoundDeck() \
            .shuffleRoundDeck() \
            .simulatePlayersDrawing() \
            .playFirstHand()

        # TODO: assert some stuff
        assert 1 == 0

    # Have people start playing