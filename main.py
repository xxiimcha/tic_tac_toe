from src.tic_tac_toe import TicTacToe

if __name__ == "__main__":
    size = int(input("Enter board size (e.g., 3 for 3x3, 5 for 5x5): "))
    win_length = int(input(f"Enter winning sequence length (1-{size}): "))
    
    game = TicTacToe(size, win_length)
    game.play()
