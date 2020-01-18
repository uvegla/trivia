from unittest2 import TestCase

from trivia import BufferedLogger, main_loop


def read_test_output(filename: str):
    lines = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())

    return lines


class MainLoopTestCase(TestCase):
    def setUp(self) -> None:
        self.logger = BufferedLogger()

    def test_1(self):
        main_loop(1, self.logger)

        self.assertEqual(self.logger.lines, read_test_output('test_1.txt'))

    def test_2(self):
        main_loop(2, self.logger)

        self.assertEqual(self.logger.lines, read_test_output('test_2.txt'))

    def test_512(self):
        main_loop(512, self.logger)

        self.assertEqual(self.logger.lines, read_test_output('test_512.txt'))
