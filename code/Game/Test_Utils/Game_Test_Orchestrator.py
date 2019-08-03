from code.Game.Modules.Player import Player
from code.Game.Test_Utils.Fake_Ranomizer import Fake_Randomizer
from code.Game.Modules.Game import Game

class Game_Test_Orchestrator(object):
    game = False  # type: Game

    def startGame(self, randomizer=False):
        if not randomizer:
            randomizer = Fake_Randomizer()
        self.game = Game(randomizer=randomizer)
        return self

    def registerPlayers(self):
        self.game.registerPlayer(Player('Ted'))
        self.game.registerPlayer(Player('Mary'))
        self.game.registerPlayer(Player('Kevin'))
        self.game.registerPlayer(Player('Kathee'))
        return self

    def startRound(self):
        self.game.startRound()
        return self

    def determineStartPlayer(self):
        self.game.currentRound.determineStartDrawPlayer()
        return self

    def initializeRoundDeck(self):
        self.game.currentRound.initializeDeck()
        return self

    def shuffleRoundDeck(self):
        self.game.currentRound.shuffleDeck()
        return self

    def simulatePlayersDrawing(self):
        round = self.game.currentRound

        while not round.deck.isEmpty():  # todo while deck isn't empty?
            round.drawFromDeckForCurrentPlayer()
            prevPlayer = round.currentDrawPlayerIndex - 1 % len(round.players)
            prevPlayerHand = round.players[prevPlayer].hand
            if prevPlayerHand[len(prevPlayerHand) - 1].number == round.trumpNumber and round.trumpSuit is False:
                round.declareTrumpSuitByPlayer(round.players[prevPlayer], [prevPlayerHand[len(prevPlayerHand) - 1]])
                # TODO only do this once, or do it more interestingly
            # TODO deterministic point at which we check that we can jump AND then do it
        return self

    def playFirstHand(self):
        # TODO simulate playing first hand
        assert 1 == 0
