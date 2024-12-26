import random
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
import sys


class SudokuCell(QPushButton):
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col
        self.value = 0
        self.initial = False  # Whether this cell is part of the initial puzzle or filled by the user
        self.setFont(self.font())  # Set a default font
        self.setStyleSheet(self.getCellStyle())

    def getCellStyle(self):
        # Define more fancy cell styling
        style = '''
            QPushButton {
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                width: 50px;
                height: 50px;
                border: 2px solid #ccc;
                background-color: #f9f9f9;
                color: #333;
                border-radius: 5px;
                outline: none;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            '''
        if (self.row % 3 == 0 and self.row != 0) or (self.col % 3 == 0 and self.col != 0):
            style += 'border-top: 3px solid black; border-left: 3px solid black;'
        return style

    def updateDisplay(self):
        if self.value == 0:
            self.setText("")
        else:
            self.setText(str(self.value))

    def setInitial(self, initial: bool):
        self.initial = initial
        if self.initial:
            self.setStyleSheet(self.getCellStyle())
        else:
            self.setStyleSheet(self.getCellStyle() + 'background-color: #ffffff;')


class SudokuGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku")
        self.setStyleSheet("background-color: #f3f3f3;")  # Set background color for the window
        self.board = [[0] * 9 for _ in range(9)]
        self.cells = [[None] * 9 for _ in range(9)]
        self.selected_cell = None
        self.history = []  # To store history of moves
        self.initUI()
        self.initGame()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        grid = QGridLayout()
        grid.setSpacing(3)

        for i in range(9):
            for j in range(9):
                cell = SudokuCell(i, j)
                cell.clicked.connect(lambda checked, row=i, col=j: self.cellClicked(row, col))
                self.cells[i][j] = cell
                grid.addWidget(cell, i, j)

        layout.addLayout(grid)

        # Buttons for solve and reset functionality
        button_layout = QHBoxLayout()

        solve_button = QPushButton("Solve Automatically")
        solve_button.setStyleSheet('background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;')
        solve_button.clicked.connect(self.solvePuzzle)
        button_layout.addWidget(solve_button)

        reset_button = QPushButton("Reset Grid")
        reset_button.setStyleSheet('background-color: #f44336; color: white; padding: 10px; border-radius: 5px;')
        reset_button.clicked.connect(self.resetGrid)
        button_layout.addWidget(reset_button)

        step_button = QPushButton("Step Through Moves")
        step_button.setStyleSheet('background-color: #2196F3; color: white; padding: 10px; border-radius: 5px;')
        step_button.clicked.connect(self.stepThroughMoves)
        button_layout.addWidget(step_button)

        layout.addLayout(button_layout)

    def initGame(self):
        self.generatePuzzle()
        self.updateDisplay()

    def generatePuzzle(self):
        self.solveSudoku()

        # Remove cells to create puzzle
        cells_to_remove = 45
        while cells_to_remove > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                saved_value = self.board[row][col]
                self.board[row][col] = 0
                self.cells[row][col].value = 0
                self.cells[row][col].setInitial(False)
                cells_to_remove -= 1

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.cells[i][j].setInitial(True)

    def cellClicked(self, row, col):
        self.selected_cell = self.cells[row][col]
        self.selected_cell.setFocus()

    def keyPressEvent(self, event):
        if self.selected_cell and not self.selected_cell.initial:
            if Qt.Key_1 <= event.key() <= Qt.Key_9:
                num = event.key() - Qt.Key_0
                if self.isValidMove(self.selected_cell.row, self.selected_cell.col, num):
                    self.board[self.selected_cell.row][self.selected_cell.col] = num
                    self.selected_cell.value = num
                    self.selected_cell.updateDisplay()
                    self.history.append((self.selected_cell.row, self.selected_cell.col, num))  # Save move
                else:
                    print(f"Invalid move: {num} at ({self.selected_cell.row}, {self.selected_cell.col})")
            elif event.key() in [Qt.Key_0, Qt.Key_Delete, Qt.Key_Backspace]:
                self.board[self.selected_cell.row][self.selected_cell.col] = 0
                self.selected_cell.value = 0
                self.selected_cell.updateDisplay()

    def updateDisplay(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].value = self.board[i][j]
                self.cells[i][j].updateDisplay()

    def isValidMove(self, row, col, num):
        for j in range(9):
            if self.board[row][j] == num and j != col:
                return False
        for i in range(9):
            if self.board[i][col] == num and i != row:
                return False
        box_row = row - row % 3
        box_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if (self.board[box_row + i][box_col + j] == num and
                        (box_row + i != row or box_col + j != col)):
                    return False
        return True

    def solveSudoku(self):
        empty = self.findEmptyCell()  # Calls the new method to find the next empty cell
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if self.isValidMove(row, col, num):
                self.board[row][col] = num
                if self.solveSudoku():
                    return True
                self.board[row][col] = 0
        return False

    def solvePuzzle(self):
        if self.solveSudoku():
            self.updateDisplay()

    def resetGrid(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.history.clear()  # Clear history of moves
        self.generatePuzzle()
        self.updateDisplay()

    def stepThroughMoves(self):
        if self.history:
            row, col, num = self.history.pop()  # Get last move
            self.board[row][col] = num
            self.cells[row][col].value = num
            self.cells[row][col].updateDisplay()

    # New method: find the next empty cell
    def findEmptyCell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None  # No empty cells found


def main():
    app = QApplication(sys.argv)
    game = SudokuGame()
    game.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
