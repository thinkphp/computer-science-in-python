import tkinter as tk
import random

class Tetris:
    def __init__(self, master):
        self.master = master
        self.master.title("Tetris")
        self.canvas = tk.Canvas(self.master, width=300, height=600)
        self.canvas.pack()

        self.grid_size = 30
        self.grid_width = 10
        self.grid_height = 20

        self.shapes = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1, 1], [0, 0, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]]
        ]

        self.colors = ['cyan', 'yellow', 'purple', 'blue', 'orange', 'green', 'red']

        self.board = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.current_piece = self.new_piece()

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Up>", self.rotate)

        self.game_loop()

    def new_piece(self):
        shape = random.choice(self.shapes)
        color = random.choice(self.colors)
        return {
            'shape': shape,
            'color': color,
            'x': self.grid_width // 2 - len(shape[0]) // 2,
            'y': 0
        }

    def draw_piece(self, piece):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_block(piece['x'] + x, piece['y'] + y, piece['color'])

    def draw_block(self, x, y, color):
        x1 = x * self.grid_size
        y1 = y * self.grid_size
        x2 = x1 + self.grid_size
        y2 = y1 + self.grid_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="white")

    def draw_board(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_block(x, y, cell)

    def move_left(self, event):
        self.current_piece['x'] -= 1
        if self.check_collision():
            self.current_piece['x'] += 1

    def move_right(self, event):
        self.current_piece['x'] += 1
        if self.check_collision():
            self.current_piece['x'] -= 1

    def move_down(self, event):
        self.current_piece['y'] += 1
        if self.check_collision():
            self.current_piece['y'] -= 1
            self.lock_piece()

    def rotate(self, event):
        original_shape = self.current_piece['shape']
        self.current_piece['shape'] = list(zip(*self.current_piece['shape'][::-1]))
        if self.check_collision():
            self.current_piece['shape'] = original_shape

    def check_collision(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    board_x = self.current_piece['x'] + x
                    board_y = self.current_piece['y'] + y
                    if (board_x < 0 or board_x >= self.grid_width or
                        board_y >= self.grid_height or
                        (board_y >= 0 and self.board[board_y][board_x])):
                        return True
        return False

    def lock_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_piece['y'] + y][self.current_piece['x'] + x] = self.current_piece['color']
        self.clear_lines()
        self.current_piece = self.new_piece()
        if self.check_collision():
            self.game_over()

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for line in lines_to_clear:
            del self.board[line]
            self.board.insert(0, [0 for _ in range(self.grid_width)])

    def game_over(self):
        self.canvas.create_text(150, 300, text="Game Over", font=("Arial", 24), fill="red")

    def game_loop(self):
        self.draw_board()
        self.draw_piece(self.current_piece)
        self.move_down(None)
        self.master.after(500, self.game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    game = Tetris(root)
    root.mainloop()
