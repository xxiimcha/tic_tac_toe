import random

class GameBoard:
    def __init__(self, size=3, win_length=None):
        """
        Initializes the game board with a given size.
        :param size: The size of the Tic-Tac-Toe board (default is 3x3).
        :param win_length: The length of the sequence required to win. Defaults to board size.
        """
        self.size = size
        self.win_length = win_length if win_length else size  # Default to full row/column/diagonal
        self.empty = " "
        self.board = [[self.empty for _ in range(size)] for _ in range(size)]  # 2D list

    def print_board(self):
        """Prints the Tic-Tac-Toe board in a structured format."""
        print("\nCurrent Board:")
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < self.size - 1:
                print("-" * (self.size * 3))

    def is_full(self):
        """Checks if the board is full (no empty spaces left)."""
        return all(cell != self.empty for row in self.board for cell in row)

    def is_winner(self, player):
        """Checks if a player has won with a sequence of at least 'win_length'."""
        def check_sequence(sequence):
            """Checks if any subset of length 'win_length' in the sequence contains only the player's marks."""
            for i in range(len(sequence) - self.win_length + 1):
                if all(self.board[r][c] == player for r, c in sequence[i:i + self.win_length]):
                    return True
            return False

        win_conditions = []

        # Rows & Columns
        for i in range(self.size):
            win_conditions.append([(i, j) for j in range(self.size)])  # Row
            win_conditions.append([(j, i) for j in range(self.size)])  # Column

        # Diagonals
        win_conditions.append([(i, i) for i in range(self.size)])  # Main diagonal
        win_conditions.append([(i, self.size - 1 - i) for i in range(self.size)])  # Anti-diagonal

        # Check all conditions
        return any(check_sequence(condition) for condition in win_conditions)

    def make_move(self, row, col, player):
        """
        Places a move on the board if the selected spot is empty.
        :return: True if move is successful, False otherwise.
        """
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == self.empty:
            self.board[row][col] = player
            return True
        return False

    def reset_board(self):
        """Resets the board for a new game."""
        self.board = [[self.empty for _ in range(self.size)] for _ in range(self.size)]
