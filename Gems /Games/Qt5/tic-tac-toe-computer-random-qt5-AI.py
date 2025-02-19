from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                           QGridLayout, QLabel, QMessageBox, QVBoxLayout, QComboBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class TicTacToeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe vs AI")
        self.setFixedSize(400, 500)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create difficulty selector
        self.difficulty_label = QLabel("AI Difficulty:")
        self.difficulty_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.difficulty_label)
        
        self.difficulty_selector = QComboBox()
        self.difficulty_selector.addItems(["Easy", "Medium", "Hard"])
        self.difficulty_selector.setCurrentText("Hard")
        layout.addWidget(self.difficulty_selector)
        
        # Create info label
        self.info_label = QLabel("You are X, AI is O")
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
        if self.check_winner(self.board, 'X'):
            QMessageBox.information(self, "Game Over", "You win!")
            self.reset_game()
            return
            
        # Check for draw
        if self.is_board_full():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_game()
            return
            
        # AI's turn
        self.ai_move()

    def ai_move(self):
        difficulty = self.difficulty_selector.currentText()
        
        if difficulty == "Easy":
            # Easy mode: 70% random, 30% smart
            import random
            if random.random() < 0.7:
                available_moves = self.get_available_moves()
                if available_moves:
                    position = random.choice(available_moves)
            else:
                position = self.get_best_move()
        elif difficulty == "Medium":
            # Medium mode: 30% random, 70% smart
            import random
            if random.random() < 0.3:
                available_moves = self.get_available_moves()
                if available_moves:
                    position = random.choice(available_moves)
            else:
                position = self.get_best_move()
        else:  # Hard mode
            position = self.get_best_move()

        self.buttons[position].setText('O')
        self.board[position] = 'O'
        
        # Check if AI wins
        if self.check_winner(self.board, 'O'):
            QMessageBox.information(self, "Game Over", "AI wins!")
            self.reset_game()
            return
            
        # Check for draw
        if self.is_board_full():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_game()
            return

    def get_best_move(self):
        best_score = float('-inf')
        best_move = None
        
        for i, spot in enumerate(self.board):
            if spot == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                
                if score > best_score:
                    best_score = score
                    best_move = i
        
        return best_move

    def minimax(self, board, depth, is_maximizing):
        # Check terminal states
        if self.check_winner(board, 'O'):
            return 1
        if self.check_winner(board, 'X'):
            return -1
        if ' ' not in board:
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for i, spot in enumerate(board):
                if spot == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i, spot in enumerate(board):
                if spot == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, board, player):
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True
        
        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True
        
        # Check diagonals
        if board[0] == board[4] == board[8] == player:
            return True
        if board[2] == board[4] == board[6] == player:
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
