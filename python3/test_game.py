from unittest2 import TestCase
from mock import Mock

from player import Player
from trivia import Game, BufferedLogger


class GameTests(TestCase):

    def setUp(self) -> None:
        self.board = Mock()
        self.players = [Player('First'), Player('Second')]
        self.logger = BufferedLogger()
        self.game = Game(self.board, self.players, self.logger)

    def test_askQuestion_printsCategoryAndQuestion(self):

        self.board.get_category.return_value = 'TestCategory'
        self.board.get_question.return_value = 'TestQuestion'
        position = 5
        self.game.ask_question(position)
        self.assertEqual('The category is TestCategory', self.logger.lines[-2])
        self.assertEqual('TestQuestion', self.logger.lines[-1])
        self.board.get_category.assert_called_with(position)
        self.board.get_question.assert_called_with('TestCategory')

    def test_roll_printsCurrentPlayerAndRolledAmount(self):
        self.game.roll(10)
        self.assertEqual('First is the current player', self.logger.lines[0])
        self.assertEqual('They have rolled a 10', self.logger.lines[1])

    def test_roll_printsNewLocationAndQuestion(self):
        self.board.get_category.return_value = 'TestCategory'
        self.board.get_question.return_value = 'TestQuestion'
        self.game.roll(10)
        self.assertEqual("First's new location is 10", self.logger.lines[-3])
        self.assertEqual('The category is TestCategory', self.logger.lines[-2])
        self.assertEqual('TestQuestion', self.logger.lines[-1])
