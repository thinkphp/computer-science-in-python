import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class ConnectFourGame(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.rows = 6
        self.cols = 7
        self.cell_size = 100
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = "red"  # Alternate between "red" and "yellow"

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setFixedSize(self.cols * self.cell_size + 5, self.rows * self.cell_size + 5)

        self.draw_board()
        self.setMouseTracking(True)

    def draw_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size
                y = row * self.cell_size
                self.scene.addRect(x, y, self.cell_size, self.cell_size, Qt.black, QColor("blue"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            col = event.x() // self.cell_size
            if col >= self.cols:
                return

            row = self.get_empty_row(col)
            if row is not None:
                self.place_piece(row, col)
                if self.check_winner(row, col):
                    self.game_over()
                else:
                    self.switch_player()

    def get_empty_row(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] is None:
                return row
        return None

    def place_piece(self, row, col):
        x = col * self.cell_size
        y = row * self.cell_size
        color = QColor(self.current_player)
        piece = QGraphicsEllipseItem(x + 5, y + 5, self.cell_size - 10, self.cell_size - 10)
        piece.setBrush(color)
        self.scene.addItem(piece)
        self.board[row][col] = self.current_player

    def switch_player(self):
        self.current_player = "yellow" if self.current_player == "red" else "red"

    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            count += self.count_direction(row, col, dr, dc)
            count += self.count_direction(row, col, -dr, -dc)
            if count >= 4:
                return True
        return False

    def count_direction(self, row, col, dr, dc):
        count = 0
        color = self.board[row][col]
        r, c = row + dr, col + dc
        while 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == color:
            count += 1
            r += dr
            c += dc
        return count

    def game_over(self):
        QMessageBox.information(self, "Game Over", f"{self.current_player.capitalize()} wins!")
        self.reset_game()

    def reset_game(self):
        self.scene.clear()
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = "red"
        self.draw_board()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = ConnectFourGame()
    game.show()
    sys.exit(app.exec_())
