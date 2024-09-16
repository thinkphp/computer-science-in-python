import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables to keep track of the game state
current_player = "X"
board = [""] * 9  # Representing the 3x3 board
buttons = []

# Function to check if there is a winner or a tie
def check_winner():
    global board
    # Define winning combinations
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    # Check for a winner
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]

    # Check for a tie
    if "" not in board:
        return "Tie"

    return None

# Function to handle button clicks
def button_click(index):
    global current_player, board

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        winner = check_winner()

        if winner:
            if winner == "Tie":
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")

# Create the buttons for the Tic-Tac-Toe board
for i in range(9):
    button = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Run the main event loop
root.mainloop()
