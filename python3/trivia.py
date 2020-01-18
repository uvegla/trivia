#!/usr/bin/env python3
import abc
import random
from random import randrange
from typing import List

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
    def __init__(self, logger: Logger):
        self.logger = logger

        self.players: List[Player] = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.staying_penalty_box = True

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def add(self, player: Player):
        self.players.append(player)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        self.logger.print(player.name + " was added")
        self.logger.print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def move_player(self, player_id: int, roll: int):
        self.places[player_id] = self.places[player_id] + roll
        if self.places[player_id] > 11:
            self.places[player_id] = self.places[player_id] - 12

        self.logger.print(self.players[player_id].name +
                          '\'s new location is ' +
                          str(self.places[player_id]))

    def roll(self, roll):
        self.logger.print("%s is the current player" %
                          self.players[self.current_player])
        self.logger.print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            self.staying_penalty_box = roll % 2 == 0
            if self.staying_penalty_box:
                self.logger.print("%s is not getting out of the penalty box" % self.players[self.current_player])
                return

            self.logger.print("%s is getting out of the penalty box" %
                              self.players[self.current_player])

        self.move_player(self.current_player, roll)
        self._ask_question()

    def _ask_question(self):
        current_position = self.places[self.current_player]
        category = self.get_category(current_position)
        self.logger.print("The category is %s" % category)
        if category == 'Pop':
            self.logger.print(self.pop_questions.pop(0))
        if category == 'Science':
            self.logger.print(self.science_questions.pop(0))
        if category == 'Sports':
            self.logger.print(self.sports_questions.pop(0))
        if category == 'Rock':
            self.logger.print(self.rock_questions.pop(0))

    def get_category(self, position):
        if position == 0:
            return 'Pop'
        if position == 4:
            return 'Pop'
        if position == 8:
            return 'Pop'
        if position == 1:
            return 'Science'
        if position == 5:
            return 'Science'
        if position == 9:
            return 'Science'
        if position == 2:
            return 'Sports'
        if position == 6:
            return 'Sports'
        if position == 10:
            return 'Sports'
        return 'Rock'

    def add_coin(self, player_id):
        self.purses[player_id] += 1
        self.logger.print(self.players[player_id].name + ' now has ' + str(self.purses[player_id]) + ' Gold Coins.')

    def next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player] and self.staying_penalty_box:
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
            self.players[self.current_player].name + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.next_player()
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


def main_loop(seed: int = None, logger: Logger = ConsoleLogger()):
    random.seed(a=seed)

    game = Game(logger)

    game.add(Player('Chet'))
    game.add(Player('Pat'))
    game.add(Player('Sue'))

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
