import unittest
from src.Game.Modules.Round import Round
from src.Game.Modules.Card import Card
from src.Game.Modules.Player import Player
from src.Game.Modules import CardConstants

class Round_Test(unittest.TestCase):
    round = False  # type: Round
    players = False  # type: List[Player]
    p1 = False  # type: Player
    p2 = False  # type: Player

    def setUp(self):
        self.p1 = Player(
            'Ted',
            [
                Card(CardConstants.SPADE, CardConstants.THREE),
                Card(CardConstants.SPADE, CardConstants.THREE),
                Card(CardConstants.SPADE, CardConstants.FOUR),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE)
            ]
        )
        self.p2 = Player(
            'Mary',
            [
                Card(CardConstants.HEART, CardConstants.THREE),
                Card(CardConstants.HEART, CardConstants.THREE),
                Card(CardConstants.HEART, CardConstants.THREE),
                Card(CardConstants.HEART, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE)
            ]
        )
        self.players = [self.p1, self.p2]
        self.round = Round(trumpNumber=CardConstants.THREE, players=self.players)

    # trump num 2 declare w 3
    def test_declare_trump_suit_wrong_number(self):
        with self.assertRaises(ValueError) as context:
            self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.FOUR)])
        assert context.exception.args[0] == Round.NOT_TRUMP_NUMBER_ERROR

    # 2 club 3 heart
    def test_declare_trump_suit_invalid_set_of_cards(self):
        with self.assertRaises(ValueError) as context:
            self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE), Card(CardConstants.SPADE, CardConstants.FOUR)])
        assert context.exception.args[0] == Round.TRUMP_DECLARATION_MISMATCH_ERROR

    def test_declare_trump_suit_player_not_in_game(self):
        with self.assertRaises(ValueError) as context:
            self.round.declareTrumpSuitByPlayer(Player('Kevin'), [Card(CardConstants.SPADE, CardConstants.THREE)])
        assert context.exception.args[0] == Round.INVALID_PLAYER_ERROR

    def test_redeclare_with_same_number(self):
        with self.assertRaises(ValueError) as context:
            self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
            self.round.declareTrumpSuitByPlayer(self.p2, [Card(CardConstants.HEART, CardConstants.THREE)])
        assert context.exception.args[0] == Round.MORE_TO_REDECLARE_ERROR

    def test_redeclare_with_fewer_but_previous_declaration(self):
        with self.assertRaises(ValueError) as context:
            self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
            self.round.declareTrumpSuitByPlayer(self.p2, [Card(CardConstants.HEART, CardConstants.THREE), Card(CardConstants.HEART, CardConstants.THREE)])
            self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
        assert context.exception.args[0] == Round.MORE_IF_PREVIOUSLY_DECLARED_ERROR

    def test_player_does_not_have_cards_to_call(self):
        with self.assertRaises(ValueError) as context:
            self.round.declareTrumpSuitByPlayer(
                self.p1,
                [
                    Card(CardConstants.SPADE, CardConstants.THREE),
                    Card(CardConstants.SPADE, CardConstants.THREE),
                    Card(CardConstants.SPADE, CardConstants.THREE)
                ]
            )
        assert context.exception.args[0] == Round.PLAYER_MISSING_CARDS_FOR_CALL_ERROR

    def test_first_valid_call_changes_game_state(self):
        self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
        assert self.round.trumpNumber == CardConstants.THREE
        assert self.round.trumpSuitDeclarationLength == 1
        assert self.round.trumpSuit == CardConstants.SPADE
        assert self.round.currentAlphaPlayerIndex == 0

    def test_first_valid_call_changes_game_state_with_already_determined_alpha(self):
        # Assumption is that unset alpha will only be in first round and tie rounds, and future rounds will be explicitly
        # set with a determined alpha player
        self.round.currentAlphaPlayerIndex = 1
        self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
        assert self.round.currentAlphaPlayerIndex == 1

    def test_second_valid_call_changes_game_state(self):
        self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
        self.round.declareTrumpSuitByPlayer(self.p2, [Card(CardConstants.HEART, CardConstants.THREE), Card(CardConstants.HEART, CardConstants.THREE)])
        assert self.round.trumpNumber == CardConstants.THREE
        assert self.round.trumpSuitDeclarationLength == 2
        assert self.round.trumpSuit == CardConstants.HEART
        assert self.round.currentAlphaPlayerIndex == 0

    def test_can_redeclare_with_previous_declaration(self):
        self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
        self.round.declareTrumpSuitByPlayer(self.p2, [Card(CardConstants.HEART, CardConstants.THREE), Card(CardConstants.HEART, CardConstants.THREE)])
        self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE), Card(CardConstants.SPADE, CardConstants.THREE)])
        assert self.round.trumpNumber == CardConstants.THREE
        assert self.round.trumpSuit == CardConstants.SPADE
        assert self.round.trumpSuitDeclarationLength == 2
        assert self.round.currentAlphaPlayerIndex == 0

    def test_can_redeclare_while_swapping_suits_multiple_times(self):
        self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE)])
        self.round.declareTrumpSuitByPlayer(self.p2, [Card(CardConstants.HEART, CardConstants.THREE), Card(CardConstants.HEART, CardConstants.THREE)])
        self.round.declareTrumpSuitByPlayer(
            self.p1,
            [
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE)
            ]
        )
        self.round.declareTrumpSuitByPlayer(
            self.p2,
            [
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE)
            ]
        )
        self.round.declareTrumpSuitByPlayer(
            self.p1,
            [
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE)
            ]
        )
        assert self.round.trumpSuit == CardConstants.DIAMOND

    def test_fails_when_trying_to_redeclare_wrong_suit(self):
        self.round.declareTrumpSuitByPlayer(self.p2, [Card(CardConstants.HEART, CardConstants.THREE)])
        self.assertTrue(self.round.trumpSuit == CardConstants.HEART, 'Trump suit is not heart after first declaration with one card')
        self.round.declareTrumpSuitByPlayer(self.p1, [Card(CardConstants.SPADE, CardConstants.THREE), Card(CardConstants.SPADE, CardConstants.THREE)])
        self.assertTrue(self.round.trumpSuit == CardConstants.SPADE, 'Trump suit is not spade after overturning with two cards')
        self.round.declareTrumpSuitByPlayer(
            self.p2,
            [
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE),
                Card(CardConstants.CLUB, CardConstants.THREE)
            ]
        )
        self.assertTrue(self.round.trumpSuit == CardConstants.CLUB, 'Trump suit is not club after overturning with three cards')
        self.round.declareTrumpSuitByPlayer(
            self.p1,
            [
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE),
                Card(CardConstants.DIAMOND, CardConstants.THREE)
            ]
        )
        self.assertTrue(self.round.trumpSuit == CardConstants.DIAMOND, 'Trump suit is not diamond after overturning with four cards')
        with self.assertRaises(ValueError) as context:
            self.round.declareTrumpSuitByPlayer(
                self.p2,
                [
                    Card(CardConstants.HEART, CardConstants.THREE),
                    Card(CardConstants.HEART, CardConstants.THREE),
                    Card(CardConstants.HEART, CardConstants.THREE),
                    Card(CardConstants.HEART, CardConstants.THREE)
                ]
            )
        self.assertTrue(
            context.exception.args[0] == Round.MORE_TO_REDECLARE_ERROR,
            'Should have thrown exception when trying to overturn 4 diamonds with 4 hearts after 3 clubs'
        )
        # Todo add more interesting assertions to this as well as the other one
