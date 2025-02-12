import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(400, 450)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)
        
        # Initialize game variables
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = []
        
        # Create status label
        self.status_label = QLabel(f"Player {self.current_player}'s turn")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont('Arial', 16))
        self.layout.addWidget(self.status_label, 0, 0, 1, 3)
        
        # Create game board buttons
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.setFont(QFont('Arial', 40))
                button.clicked.connect(lambda checked, r=row, c=col: self.make_move(r, c))
                self.layout.addWidget(button, row + 1, col)
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Create reset button
        reset_button = QPushButton("New Game")
        reset_button.setFont(QFont('Arial', 12))
        reset_button.clicked.connect(self.reset_game)
        self.layout.addWidget(reset_button, 4, 0, 1, 3)

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            
            if self.check_winner(row, col):
                self.show_winner()
            elif self.is_board_full():
                self.show_draw()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.setText(f"Player {self.current_player}'s turn")

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
            
        # Check column
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
            
        # Check diagonals
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
            
        if row + col == 2 and all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
            
        return False

    def is_board_full(self):
        return all(self.board[r][c] != '' for r in range(3) for c in range(3))

    def show_winner(self):
        QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
        self.reset_game()

    def show_draw(self):
        QMessageBox.information(self, "Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.setText('')
        self.status_label.setText(f"Player {self.current_player}'s turn")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
