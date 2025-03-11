import unittest
from src.game_board import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()

    def test_make_move(self):
        self.assertTrue(self.board.make_move(0, 0, "X"))
        self.assertFalse(self.board.make_move(0, 0, "O"))

    def test_is_winner(self):
        self.board.board = [
            ["X", "X", "X"],
            [" ", "O", "O"],
            ["O", " ", " "]
        ]
        self.assertTrue(self.board.is_winner("X"))
        self.assertFalse(self.board.is_winner("O"))

    def test_is_full(self):
        self.board.board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.board.is_full())

if __name__ == "__main__":
    unittest.main()
