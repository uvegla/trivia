from unittest2 import TestCase

from player import Player


class PlayerTestCase(TestCase):
    def setUp(self) -> None:
        self.player = Player('Frank')

    def test_str(self):
        self.assertEqual(str(self.player), self.player.name)

    def test_stay_in_place(self):
        self.player.move(0)

        self.assertEqual(self.player.position, 0)

    def test_move(self):
        self.player.move(5)

        self.assertEqual(self.player.position, 5)

    def test_loop(self):
        self.player.move(12)

        self.assertEqual(self.player.position, 0)

    def test_overflow(self):
        self.player.move(15)

        self.assertEqual(self.player.position, 3)
