import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]

        # Create game info label
        self.info_label = tk.Label(
            root,
            text="You are X, computer is O",
            font=('Arial', 12),
            pady=10
        )
        self.info_label.pack()

        # Create game board frame
        self.board_frame = tk.Frame(root)
        self.board_frame.pack()

        # Create buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text='',
                    font=('Arial', 20, 'bold'),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)

    def button_click(self, row, col):
        position = row * 3 + col

        # Check if the position is valid
        if self.board[position] != ' ':
            messagebox.showwarning("Invalid Move", "That position is already taken!")
            return

        # Update button and board
        self.buttons[position].config(text='X')
        self.board[position] = 'X'

        # Check if player wins
        if self.check_winner():
            messagebox.showinfo("Game Over", "You win!")
            self.root.quit()
            return

        # Check for draw
        if self.is_board_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.root.quit()
            return

        # Computer's turn
        self.computer_move()

    def computer_move(self):
        available_moves = self.get_available_moves()
        if available_moves:
            position = random.choice(available_moves)
            self.buttons[position].config(text='O')
            self.board[position] = 'O'

            # Check if computer wins
            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.root.quit()
                return

            # Check for draw
            if self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.quit()
                return

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True

        return False

    def is_board_full(self):
        return ' ' not in self.board

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
