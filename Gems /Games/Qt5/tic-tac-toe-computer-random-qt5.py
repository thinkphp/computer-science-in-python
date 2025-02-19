from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                           QGridLayout, QLabel, QMessageBox, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys
import random

class TicTacToeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(400, 450)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create info label
        self.info_label = QLabel("You are X, computer is O")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFont(QFont('Arial', 14))
        layout.addWidget(self.info_label)
        
        # Create game board
        board_widget = QWidget()
        self.board_layout = QGridLayout(board_widget)
        self.board_layout.setSpacing(5)
        layout.addWidget(board_widget)
        
        # Initialize game state
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        
        # Create board buttons
        for i in range(3):
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.setFont(QFont('Arial', 48, QFont.Bold))
                button.clicked.connect(lambda checked, row=i, col=j: self.button_click(row, col))
                self.board_layout.addWidget(button, i, j)
                self.buttons.append(button)
        
        # Add reset button
        reset_button = QPushButton("New Game")
        reset_button.setFont(QFont('Arial', 12))
        reset_button.clicked.connect(self.reset_game)
        layout.addWidget(reset_button)
        
        self.show()

    def button_click(self, row, col):
        position = row * 3 + col
        
        # Check if the position is valid
        if self.board[position] != ' ':
            QMessageBox.warning(self, "Invalid Move", "That position is already taken!")
            return
            
        # Update button and board
        self.buttons[position].setText('X')
        self.board[position] = 'X'
        
        # Check if player wins
        if self.check_winner():
            QMessageBox.information(self, "Game Over", "You win!")
            self.reset_game()
            return
            
        # Check for draw
        if self.is_board_full():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_game()
            return
            
        # Computer's turn
        self.computer_move()

    def computer_move(self):
        available_moves = self.get_available_moves()
        if available_moves:
            position = random.choice(available_moves)
            self.buttons[position].setText('O')
            self.board[position] = 'O'
            
            # Check if computer wins
            if self.check_winner():
                QMessageBox.information(self, "Game Over", "Computer wins!")
                self.reset_game()
                return
                
            # Check for draw
            if self.is_board_full():
                QMessageBox.information(self, "Game Over", "It's a draw!")
                self.reset_game()
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

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.setText('')

def main():
    app = QApplication(sys.argv)
    window = TicTacToeWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
