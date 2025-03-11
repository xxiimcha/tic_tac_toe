import random
from src.game_board import GameBoard

class TicTacToe:
    def __init__(self):
        self.board = GameBoard()
        self.players = ["X", "O"]
        self.current_player = random.choice(self.players)  # Randomize first player

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print(f"Player {self.current_player} starts the game!")

        while True:
            self.board.print_board()
            player = self.current_player

            # Get user move with validation
            while True:
                try:
                    row, col = map(int, input(f"Player {player}, enter row and col (0-2, space-separated): ").split())
                    if 0 <= row < 3 and 0 <= col < 3:
                        if self.board.make_move(row, col, player):
                            break
                        else:
                            print("That spot is already taken! Try again.")
                    else:
                        print("Invalid input! Row and column must be between 0 and 2.")
                except ValueError:
                    print("Invalid format! Enter row and col separated by a space (e.g., '1 2').")

            # Check for winner or tie
            if self.board.is_winner(player):
                self.board.print_board()
                print(f"🎉 Player {player} wins! 🎉")
                if self.ask_replay():
                    continue
                else:
                    break
            elif self.board.is_full():
                self.board.print_board()
                print("It's a tie! 🤝")
                if self.ask_replay():
                    continue
                else:
                    break

            self.switch_player()

    def ask_replay(self):
        """Asks if players want to restart the game."""
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            self.board.reset_board()
            self.current_player = random.choice(self.players)  # New random first player
            print("\nStarting a new game!\n")
            return True
        return False
