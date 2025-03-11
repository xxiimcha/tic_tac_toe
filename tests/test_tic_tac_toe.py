import unittest
from src.game_board import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        """Create a fresh game board before each test."""
        self.board = GameBoard()

    def test_make_move_valid(self):
        """Test that a valid move is placed on the board."""
        self.assertTrue(self.board.make_move(0, 0, "X"))
        self.assertEqual(self.board.board[0][0], "X")

    def test_make_move_invalid(self):
        """Test that an invalid move (occupied cell) is rejected."""
        self.board.make_move(0, 0, "X")
        self.assertFalse(self.board.make_move(0, 0, "O"))  # Should not overwrite X
        self.assertEqual(self.board.board[0][0], "X")  # Should still be X

    def test_is_winner_row(self):
        """Test if a player wins with a complete row."""
        self.board.board = [
            ["X", "X", "X"],
            [" ", "O", "O"],
            ["O", " ", " "]
        ]
        self.assertTrue(self.board.is_winner("X"))
        self.assertFalse(self.board.is_winner("O"))

    def test_is_winner_column(self):
        """Test if a player wins with a complete column."""
        self.board.board = [
            ["O", "X", " "],
            ["O", "X", " "],
            ["O", "X", " "]
        ]
        self.assertTrue(self.board.is_winner("X"))
        self.assertTrue(self.board.is_winner("O"))

    def test_is_winner_diagonal(self):
        """Test if a player wins with a diagonal line."""
        self.board.board = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", "O", "X"]
        ]
        self.assertTrue(self.board.is_winner("X"))
        self.assertFalse(self.board.is_winner("O"))

    def test_is_tie(self):
        """Test if the game detects a tie correctly."""
        self.board.board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.board.is_full())  # Board is full
        self.assertFalse(self.board.is_winner("X"))  # No winner
        self.assertFalse(self.board.is_winner("O"))

    def test_reset_board(self):
        """Ensure board resets properly."""
        self.board.make_move(1, 1, "X")  # Make a move
        self.board.reset_board()
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, self.board.empty)  # Should be empty again

if __name__ == "__main__":
    unittest.main()
