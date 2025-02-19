import random

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

def get_available_moves(board):
    """Get list of empty positions on the board."""
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm for finding the best move.
    Returns score of the board position.
    """
    winner = check_winner(board)
    if winner == 'O':
        return 10 - depth
    if winner == 'X':
        return depth - 10
    if is_board_full(board):
        return 0

    available_moves = get_available_moves(board)
    
    if is_maximizing:
        best_score = float('-inf')
        for move in available_moves:
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in available_moves:
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def computer_move(board):
    """Make the best move for the computer using minimax algorithm."""
    best_score = float('-inf')
    best_move = None
    available_moves = get_available_moves(board)
    
    # If it's the first move, randomly choose a corner or center
    if len(available_moves) == 9:
        return random.choice([0, 2, 4, 6, 8])
    
    for move in available_moves:
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move

def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    print("You are X, computer (AI) is O")
    print("Positions are numbered from 1-9, left to right, top to bottom.")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()

    while True:
        print_board(board)
        
        if current_player == 'X':
            position = input(f"Your turn! Enter position (1-9): ")
            # Input validation
            if not position.isdigit() or not 1 <= int(position) <= 9:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
            position = int(position) - 1
            if board[position] != ' ':
                print("That position is already taken! Try again.")
                continue
        else:
            print("AI is thinking...")
            position = computer_move(board)
        
        # Make move
        board[position] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print("Congratulations! You win!")
            else:
                print("AI wins!")
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
