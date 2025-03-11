from src.game_board import GameBoard

class TicTacToe:
    def __init__(self, size=3, win_length=None):
        self.board = GameBoard(size, win_length)
        self.players = ["X", "O"]
        self.current_player = self.players[0]

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print(f"Board Size: {self.board.size}x{self.board.size}, Winning Sequence: {self.board.win_length}")
        while True:
            self.board.print_board()
            player = self.current_player

            # Get user move with validation
            while True:
                try:
                    row, col = map(int, input(f"Player {player}, enter row and col (0-{self.board.size - 1}, space-separated): ").split())
                    if 0 <= row < self.board.size and 0 <= col < self.board.size:
                        if self.board.make_move(row, col, player):
                            break
                        else:
                            print("That spot is already taken! Try again.")
                    else:
                        print(f"Invalid input! Row and column must be between 0 and {self.board.size - 1}.")
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
            self.current_player = self.players[0]
            print("\nStarting a new game!\n")
            return True
        return False
