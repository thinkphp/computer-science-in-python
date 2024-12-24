import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QMessageBox)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QSize

class GomokuGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.board_size = 15
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.current_player = 1  # 1 for black, 2 for white
        self.game_over = False

    def initUI(self):
        self.setWindowTitle('Gomoku')
        self.setGeometry(100, 100, 800, 700)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()

        # Game board widget
        self.board_widget = BoardWidget(self)
        main_layout.addWidget(self.board_widget)

        # Side panel
        side_panel = QWidget()
        side_layout = QVBoxLayout()

        # Player turn label
        self.turn_label = QLabel(f"Current Player: Black")
        side_layout.addWidget(self.turn_label)

        # New Game button
        new_game_btn = QPushButton("New Game")
        new_game_btn.clicked.connect(self.reset_game)
        side_layout.addWidget(new_game_btn)

        side_panel.setLayout(side_layout)
        main_layout.addWidget(side_panel)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def make_move(self, row, col):
        if self.game_over or self.board[row, col] != 0:
            return

        self.board[row, col] = self.current_player
        self.board_widget.update()

        if self.check_win(row, col):
            winner = "Black" if self.current_player == 1 else "White"
            QMessageBox.information(self, "Game Over", f"{winner} wins!")
            self.game_over = True
        else:
            # Switch players
            self.current_player = 3 - self.current_player
            player_name = "Black" if self.current_player == 1 else "White"
            self.turn_label.setText(f"Current Player: {player_name}")

    def check_win(self, row, col):
        directions = [
            (0, 1),   # Horizontal
            (1, 0),   # Vertical
            (1, 1),   # Diagonal \
            (1, -1)   # Diagonal /
        ]

        for dx, dy in directions:
            count = self.count_consecutive(row, col, dx, dy) + \
                    self.count_consecutive(row, col, -dx, -dy) - 1
            if count >= 5:
                return True
        return False

    def count_consecutive(self, row, col, dx, dy):
        current = self.board[row, col]
        count = 0
        r, c = row, col
        while 0 <= r < self.board_size and 0 <= c < self.board_size and \
              self.board[r, c] == current:
            count += 1
            r += dx
            c += dy
        return count

    def reset_game(self):
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.current_player = 1
        self.game_over = False
        self.turn_label.setText("Current Player: Black")
        self.board_widget.update()

class BoardWidget(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.setFixedSize(600, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        try:
            painter.setRenderHint(QPainter.Antialiasing)

            # Draw grid
            pen = QPen(Qt.black, 1)
            painter.setPen(pen)

            cell_size = int(self.width() / self.game.board_size)
            for i in range(self.game.board_size + 1):
                x = int(i * cell_size)
                painter.drawLine(
                    x, 0,
                    x, self.height()
                )
                painter.drawLine(
                    0, x,
                    self.width(), x
                )

            # Draw stones
            for row in range(self.game.board_size):
                for col in range(self.game.board_size):
                    if self.game.board[row, col] == 1:
                        painter.setBrush(QColor(0, 0, 0))
                        painter.drawEllipse(
                            int(col * cell_size + cell_size/2 - 15),
                            int(row * cell_size + cell_size/2 - 15),
                            30, 30
                        )
                    elif self.game.board[row, col] == 2:
                        painter.setBrush(QColor(255, 255, 255))
                        painter.setPen(QPen(Qt.black, 2))
                        painter.drawEllipse(
                            int(col * cell_size + cell_size/2 - 15),
                            int(row * cell_size + cell_size/2 - 15),
                            30, 30
                        )
        finally:
            painter.end()  # Explicitly end the painter

    def mousePressEvent(self, event):
        cell_size = self.width() / self.game.board_size
        col = int(event.x() / cell_size)
        row = int(event.y() / cell_size)

        self.game.make_move(row, col)

def main():
    app = QApplication(sys.argv)
    game = GomokuGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
