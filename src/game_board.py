import random

class GameBoard:
    def __init__(self):
        self.empty = " "
        self.board = [[self.empty for _ in range(3)] for _ in range(3)]  # 2D list for a 3x3 board

    def print_board(self):
        print("\nCurrent Board:")
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:
                print("-" * 9)

    def is_full(self):
        return all(cell != self.empty for row in self.board for cell in row)

    def is_winner(self, player):
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)],  # Rows
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],  # Columns
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],  # Diagonals
            [(0, 2), (1, 1), (2, 0)]
        ]
        return any(all(self.board[r][c] == player for r, c in condition) for condition in win_conditions)

    def make_move(self, row, col, player):
        if self.board[row][col] == self.empty:
            self.board[row][col] = player
            return True
        return False

    def reset_board(self):
        """Resets the board for a new game."""
        self.board = [[self.empty for _ in range(3)] for _ in range(3)]
