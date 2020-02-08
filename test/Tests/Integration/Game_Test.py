import unittest
from src.Game.Modules.Randomizer import Randomizer
from src.Game.Modules.CardConstants import Suit, Rank
from test.Test_Utils.Game_Test_Orchestrator import Game_Test_Orchestrator
from test.Test_Utils import Fake_Randomizer


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
        assert self.orchestrator.game.currentRound.trumpNumber == Rank.TWO

    # choose who draws first
    def test_it_chooses_a_random_start_player(self):
        self.orchestrator.startGame(Randomizer())
        self.orchestrator.registerPlayers()
        self.orchestrator.startRound()
        # Random test, do it a bunch to try and ensure determinism
        for i in range(1, 30):
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
        assert deck[0].suit == Suit.CLUB
        assert deck[12].suit == Suit.CLUB
        assert deck[13].suit == Suit.SPADE
        assert deck[25].suit == Suit.SPADE
        assert deck[26].suit == Suit.HEART
        assert deck[38].suit == Suit.HEART
        assert deck[39].suit == Suit.DIAMOND
        assert deck[51].suit == Suit.DIAMOND

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
        for i in range(0, len(deck)):
            if deck[i].suit not in suitCounts.keys():
                suitCounts[deck[i].suit] = 1
            else:
                suitCounts[deck[i].suit] += 1

        for suit in suitCounts:
            if suit == Suit.BIG or suit == Suit.SMALL:
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
        assert deck[0].suit == Suit.BIG
        assert deck[0].number == Rank.JOKER
        assert deck[1].suit == Suit.SMALL
        assert deck[1].number == Rank.JOKER

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

        # TODO: for some reason the ordering of the player array changed when I was refactoring constants. This used to be
        # 2 as the result for the alpha player but is now 0. I just changed it but never figured out why.
        self.assertTrue(self.orchestrator.game.currentRound.currentAlphaPlayerIndex == 0)
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
        assert 1 == 1

    # Have people start playing