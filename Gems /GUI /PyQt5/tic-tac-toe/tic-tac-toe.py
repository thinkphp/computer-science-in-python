import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 400)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Status label
        self.status_label = QLabel("Player X's Turn")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont('Arial', 16))
        main_layout.addWidget(self.status_label)

        # Game board layout
        board_layout = QGridLayout()
        self.buttons = []
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
        # Check if the button is already played
        if self.buttons[row][col].text():
            return

        # Set button text to current player
        self.buttons[row][col].setText(self.current_player)

        # Check for winner
        if self.check_winner(row, col):
            self.status_label.setText(f"Player {self.current_player} Wins!")
            self.disable_buttons()
            return

        # Check for draw
        if self.check_draw():
            self.status_label.setText("It's a Draw!")
            return

        # Switch players
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.setText(f"Player {self.current_player}'s Turn")

    def check_winner(self, row, col):
        # Check row
        if all(self.buttons[row][c].text() == self.current_player for c in range(3)):
            return True

        # Check column
        if all(self.buttons[r][col].text() == self.current_player for r in range(3)):
            return True

        # Check diagonals
        if row == col and all(self.buttons[i][i].text() == self.current_player for i in range(3)):
            return True

        if row + col == 2 and all(self.buttons[i][2-i].text() == self.current_player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.buttons[r][c].text() != ''
                   for r in range(3)
                   for c in range(3))

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def reset_game(self):
        # Reset all buttons
        for row in self.buttons:
            for button in row:
                button.setText('')
                button.setEnabled(True)

        # Reset game state
        self.current_player = 'X'
        self.status_label.setText("Player X's Turn")

def main():
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
