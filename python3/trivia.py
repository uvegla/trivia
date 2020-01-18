#!/usr/bin/env python3
import abc
import random
from itertools import cycle
from random import randrange
from typing import List

from board import Board
from player import Player


class Logger:
    @abc.abstractmethod
    def print(self, msg: str):
        pass


class ConsoleLogger(Logger):
    def print(self, msg: str):
        print(msg)


class BufferedLogger(Logger):
    def __init__(self):
        super(BufferedLogger, self).__init__()
        self.lines = []

    def print(self, msg: str):
        self.lines.append(msg)


class Game:
    def __init__(self, board: Board, players: List[Player], logger: Logger):
        self.logger = logger

        self.players = players
        self.board = board

        for i, player in enumerate(players, 1):
            self.logger.print(player.name + " was added")
            self.logger.print("They are player number %s" % i)

        self.cycle = cycle(self.players)
        self.current_player: Player = next(self.cycle)

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.staying_penalty_box = True

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    @property
    def how_many_players(self):
        return len(self.players)

    def move_player(self, player: Player, roll: int):
        player.move(roll)
        self.logger.print(player.name + '\'s new location is ' + str(player.position))

    def roll(self, roll):
        self.logger.print("%s is the current player" % self.current_player)
        self.logger.print("They have rolled a %s" % roll)

        if self.current_player.in_penalty_box:
            self.staying_penalty_box = roll % 2 == 0
            if self.staying_penalty_box:
                self.logger.print("%s is not getting out of the penalty box" % self.current_player)
                return

            self.logger.print("%s is getting out of the penalty box" % self.current_player)

        self.move_player(self.current_player, roll)
        self.ask_question(self.current_player.position)

    def ask_question(self, current_position):
        category = self.board.get_category(current_position)
        self.logger.print("The category is %s" % category)
        self.logger.print(self.board.get_question(category))

    def add_coin(self, player_id):
        self.current_player.purse += 1
        self.logger.print(self.current_player.name + ' now has ' + str(self.current_player.purse) + ' Gold Coins.')

    def next_player(self):
        # noinspection PyAttributeOutsideInit
        self.current_player = next(self.cycle)

    def was_correctly_answered(self):
        if self.current_player.in_penalty_box and self.staying_penalty_box:
            self.next_player()
            return True

        self.logger.print("Answer was correct!!!!")
        self.add_coin(self.current_player)

        winner = self._did_player_win()
        self.next_player()

        return winner

    def wrong_answer(self):
        self.logger.print('Question was incorrectly answered')
        self.logger.print(
            self.current_player.name + " was sent to the penalty box")

        self.current_player.in_penalty_box = True

        self.next_player()
        return True

    def _did_player_win(self):
        return not (self.current_player.purse == 6)


def main_loop(seed: int = None, logger: Logger = ConsoleLogger()):
    random.seed(a=seed)

    game = Game(Board(), [Player('Chet'), Player('Pat'), Player('Sue')], logger)

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner:
            break


if __name__ == '__main__':
    main_loop(512)
