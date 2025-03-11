from src.game_board import GameBoard

class TicTacToe:
    def __init__(self):
        self.board = GameBoard()
        self.players = ["X", "O"]
        self.current_player = 0

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def play(self):
        while True:
            self.board.print_board()
            player = self.players[self.current_player]

            # Get move from user
            while True:
                try:
                    move = int(input(f"Player {player}, enter row (0-2): ")), int(input(f"Player {player}, enter col (0-2): "))
                    if 0 <= move[0] < 3 and 0 <= move[1] < 3 and self.board.make_move(*move, player):
                        break
                except ValueError:
                    pass
                print("Invalid move, try again.")

            # Check game status
            if self.board.is_winner(player):
                self.board.print_board()
                print(f"Player {player} wins!")
                break
            elif self.board.is_full():
                self.board.print_board()
                print("It's a tie!")
                break
            
            self.switch_player()
