import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 20
BALL_SPEED = 5

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        # Paddles
        self.paddle1 = self.canvas.create_rectangle(10, 150, 10 + PADDLE_WIDTH, 150 + PADDLE_HEIGHT, fill="white")
        self.paddle2 = self.canvas.create_rectangle(WINDOW_WIDTH - 20, 150, WINDOW_WIDTH - 10, 150 + PADDLE_HEIGHT, fill="white")

        # Ball
        self.ball = self.canvas.create_oval(WINDOW_WIDTH//2 - BALL_SIZE//2, WINDOW_HEIGHT//2 - BALL_SIZE//2,
                                            WINDOW_WIDTH//2 + BALL_SIZE//2, WINDOW_HEIGHT//2 + BALL_SIZE//2, fill="white")

        # Ball movement
        self.ball_dx = BALL_SPEED * random.choice([-1, 1])
        self.ball_dy = BALL_SPEED * random.choice([-1, 1])

        # Scores
        self.score1 = 0
        self.score2 = 0
        self.score_display = self.canvas.create_text(WINDOW_WIDTH//2, 30, text="0 - 0", fill="white", font=('Helvetica', 24))

        # Bind keys
        self.root.bind("<w>", self.move_paddle1_up)
        self.root.bind("<s>", self.move_paddle1_down)
        self.root.bind("<Up>", self.move_paddle2_up)
        self.root.bind("<Down>", self.move_paddle2_down)

        # Start the game
        self.update_game()

    def move_paddle1_up(self, event):
        if self.canvas.coords(self.paddle1)[1] > 0:
            self.canvas.move(self.paddle1, 0, -PADDLE_SPEED)

    def move_paddle1_down(self, event):
        if self.canvas.coords(self.paddle1)[3] < WINDOW_HEIGHT:
            self.canvas.move(self.paddle1, 0, PADDLE_SPEED)

    def move_paddle2_up(self, event):
        if self.canvas.coords(self.paddle2)[1] > 0:
            self.canvas.move(self.paddle2, 0, -PADDLE_SPEED)

    def move_paddle2_down(self, event):
        if self.canvas.coords(self.paddle2)[3] < WINDOW_HEIGHT:
            self.canvas.move(self.paddle2, 0, PADDLE_SPEED)

    def update_game(self):
        # Ball movement
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

        ball_coords = self.canvas.coords(self.ball)
        paddle1_coords = self.canvas.coords(self.paddle1)
        paddle2_coords = self.canvas.coords(self.paddle2)

        # Ball collision with top and bottom walls
        if ball_coords[1] <= 0 or ball_coords[3] >= WINDOW_HEIGHT:
            self.ball_dy = -self.ball_dy

        # Ball collision with paddles
        if self.check_collision(ball_coords, paddle1_coords):
            self.ball_dx = -self.ball_dx
        elif self.check_collision(ball_coords, paddle2_coords):
            self.ball_dx = -self.ball_dx

        # Ball out of bounds
        if ball_coords[0] <= 0:
            self.score2 += 1
            self.reset_ball()
        elif ball_coords[2] >= WINDOW_WIDTH:
            self.score1 += 1
            self.reset_ball()

        # Update score
        self.canvas.itemconfig(self.score_display, text=f"{self.score1} - {self.score2}")

        # Loop the game
        self.root.after(30, self.update_game)

    def check_collision(self, ball, paddle):
        return (ball[0] <= paddle[2] and ball[2] >= paddle[0] and
                ball[1] <= paddle[3] and ball[3] >= paddle[1])

    def reset_ball(self):
        self.canvas.coords(self.ball, WINDOW_WIDTH//2 - BALL_SIZE//2, WINDOW_HEIGHT//2 - BALL_SIZE//2,
                           WINDOW_WIDTH//2 + BALL_SIZE//2, WINDOW_HEIGHT//2 + BALL_SIZE//2)
        self.ball_dx = BALL_SPEED * random.choice([-1, 1])
        self.ball_dy = BALL_SPEED * random.choice([-1, 1])

# Create the game window and start the game
root = tk.Tk()
game = PongGame(root)
root.mainloop()
