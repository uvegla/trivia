from unittest2 import TestCase

from board import Board


class BoardTests(TestCase):

    def setUp(self) -> None:
        self.board = Board()

    def test_getCategory_0_returnsPop(self):
        self.assertEqual('Pop', self.board.get_category(0))

    def test_getCategory_4_returnsPop(self):
        self.assertEqual('Pop', self.board.get_category(4))

    def test_getCategory_8_returnsPop(self):
        self.assertEqual('Pop', self.board.get_category(8))

    def test_getCategory_1_returnsScience(self):
        self.assertEqual('Science', self.board.get_category(1))

    def test_getCategory_5_returnsScience(self):
        self.assertEqual('Science', self.board.get_category(5))

    def test_getCategory_9_returnsScience(self):
        self.assertEqual('Science', self.board.get_category(9))

    def test_getCategory_2_returnsSports(self):
        self.assertEqual('Sports', self.board.get_category(2))

    def test_getCategory_6_returnsSports(self):
        self.assertEqual('Sports', self.board.get_category(6))

    def test_getCategory_10_returnsSports(self):
        self.assertEqual('Sports', self.board.get_category(10))

    def test_getCategory_3_returnsRock(self):
        self.assertEqual('Rock', self.board.get_category(3))

    def test_getQuestion_Pop_returnsPopQuestionZero(self):
        self.assertEqual('Pop Question 0', self.board.get_question('Pop'))

    def test_getQuestion_PopTwice_returnsPopQuestionOne(self):
        self.board.get_question('Pop')
        self.assertEqual('Pop Question 1', self.board.get_question('Pop'))

    def test_getQuestion_Science_returnsScienceQuestionZero(self):
        self.assertEqual('Science Question 0', self.board.get_question('Science'))

    def test_getQuestion_Sports_returnsSportsQuestionZero(self):
        self.assertEqual('Sports Question 0', self.board.get_question('Sports'))

    def test_getQuestion_Rock_returnsSportsQuestionZero(self):
        self.assertEqual('Rock Question 0', self.board.get_question('Rock'))
