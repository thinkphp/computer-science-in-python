import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe vs AI")
        self.setGeometry(100, 100, 300, 400)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Status label
        self.status_label = QLabel("Your Turn (X)")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont('Arial', 16))
        main_layout.addWidget(self.status_label)

        # Game board layout
        board_layout = QGridLayout()
        self.buttons = []
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        # Create 3x3 grid of buttons
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton('')
                button.setFixedSize(100, 100)
                button.setFont(QFont('Arial', 40))
                button.clicked.connect(lambda _, r=row, c=col: self.on_button_click(r, c))
                board_layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)

        # Add board layout to main layout
        main_layout.addLayout(board_layout)

        # Reset button
        reset_button = QPushButton("Reset Game")
        reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(reset_button)

        # Set main layout
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def on_button_click(self, row, col):
        # Human player's turn (X)
        if self.current_player == 'X':
            # Check if the button is already played
            if self.board[row][col] != '':
                return

            # Make move
            self.make_move(row, col, 'X')

            # Check game state
            if self.check_winner('X'):
                self.end_game("You Win!")
                return

            if self.is_board_full():
                self.end_game("Draw!")
                return

            # AI's turn
            self.current_player = 'O'
            self.status_label.setText("AI's Turn")
            QApplication.processEvents()  # Update UI

            # AI makes a move
            ai_move = self.get_ai_move()
            if ai_move:
                self.make_move(ai_move[0], ai_move[1], 'O')

                # Check AI's game state
                if self.check_winner('O'):
                    self.end_game("AI Wins!")
                    return

                if self.is_board_full():
                    self.end_game("Draw!")
                    return

                # Back to human player
                self.current_player = 'X'
                self.status_label.setText("Your Turn (X)")

    def make_move(self, row, col, player):
        # Update board state
        self.board[row][col] = player
        self.buttons[row][col].setText(player)

    def get_ai_move(self):
        # Prioritize center and corners
        if self.board[1][1] == '':
            return (1, 1)

        # Try corners
        corners = [(0,0), (0,2), (2,0), (2,2)]
        random.shuffle(corners)
        for corner in corners:
            if self.board[corner[0]][corner[1]] == '':
                return corner

        # Minimax algorithm for optimal move
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    # Try this move
                    self.board[row][col] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = ''  # Undo move

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        # Fallback to random empty space if no optimal move
        if best_move is None:
            empty_spaces = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == '']
            return random.choice(empty_spaces) if empty_spaces else None

        return best_move

    def minimax(self, board, depth, is_maximizing):
        # Check terminal states
        if self.check_winner('O'):
            return 10 - depth
        if self.check_winner('X'):
            return depth - 10
        if self.is_board_full():
            return 0

        # Maximizing player (AI)
        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ''
                        best_score = max(best_score, score)
            return best_score

        # Minimizing player (Human)
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ''
                        best_score = min(best_score, score)
            return best_score

    def check_winner(self, player):
        # Check rows
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True

        if all(self.board[i][2-i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(self.board[row][col] != ''
                   for row in range(3)
                   for col in range(3))

    def end_game(self, message):
        # Disable buttons and show message
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

        # Show message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(message)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec_()

    def reset_game(self):
        # Reset board state
        self.board = [['' for _ in range(3)] for _ in range(3)]

        # Reset all buttons
        for row in self.buttons:
            for button in row:
                button.setText('')
                button.setEnabled(True)

        # Reset game state
        self.current_player = 'X'
        self.status_label.setText("Your Turn (X)")

def main():
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
