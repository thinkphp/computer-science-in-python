import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("400x450")

        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Arial", 16))
        self.score_label.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_direction = "Right"
        self.food = self.create_food()
        self.score = 0

        self.master.bind("<KeyPress>", self.change_direction)

        self.update()

    def create_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="red", tags="food")
        return (x, y)

    def move_snake(self):
        head = self.snake[0]
        if self.snake_direction == "Right":
            new_head = (head[0] + 10, head[1])
        elif self.snake_direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.snake_direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.snake_direction == "Down":
            new_head = (head[0], head[1] + 10)

        self.snake = [new_head] + self.snake[:-1]

    def change_direction(self, event):
        key = event.keysym
        if (key == "Right" and not self.snake_direction == "Left") or \
           (key == "Left" and not self.snake_direction == "Right") or \
           (key == "Up" and not self.snake_direction == "Down") or \
           (key == "Down" and not self.snake_direction == "Up"):
            self.snake_direction = key

    def check_collisions(self):
        head = self.snake[0]
        return (
            head[0] < 0 or head[0] >= 400 or
            head[1] < 0 or head[1] >= 400 or
            head in self.snake[1:]
        )

    def update(self):
        self.move_snake()
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1],
                                         segment[0] + 10, segment[1] + 10,
                                         fill="green", tags="snake")

        if self.snake[0] == self.food:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.snake.append(self.snake[-1])
            self.canvas.delete("food")
            self.food = self.create_food()

        if self.check_collisions():
            self.canvas.create_text(200, 200, text="Game Over!", fill="white", font=("Arial", 24))
            return

        self.master.after(100, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
