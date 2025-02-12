def print_board(board):
    """Print the current state of the board."""
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")

def check_winner(board):
    """Check if there's a winner. Returns the winning player ('X' or 'O') or None."""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]

    return None

def is_board_full(board):
    """Check if the board is full."""
    return ' ' not in board

def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 1-9, left to right, top to bottom.")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()

    while True:
        print_board(board)
        position = input(f"Player {current_player}, enter position (1-9): ")

        # Input validation
        if not position.isdigit() or not 1 <= int(position) <= 9:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        position = int(position) - 1

        if board[position] != ' ':
            print("That position is already taken! Try again.")
            continue

        # Make move
        board[position] = current_player

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
