import tkinter as tk
import math

WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 20

class BouncingBall(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, width=WIDTH, height=HEIGHT, bg='white')
        self.pack()

        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.dx = 2
        self.dy = 2

        self.create_oval(self.x - BALL_RADIUS, self.y - BALL_RADIUS,
                         self.x + BALL_RADIUS, self.y + BALL_RADIUS,
                         fill='red', outline='red')

        self.update_ball()

    def update_ball(self):
        self.x += self.dx
        self.y += self.dy

        # Check for collision with window edges
        if self.x < BALL_RADIUS or self.x > WIDTH - BALL_RADIUS:
            self.dx = -self.dx
        if self.y < BALL_RADIUS or self.y > HEIGHT - BALL_RADIUS:
            self.dy = -self.dy

        # Redraw ball
        self.delete('all')
        self.create_oval(self.x - BALL_RADIUS, self.y - BALL_RADIUS,
                         self.x + BALL_RADIUS, self.y + BALL_RADIUS,
                         fill='red', outline='red')

        # Schedule next update
        self.after(16, self.update_ball)

def main():
    root = tk.Tk()
    root.title("Bouncing Ball")
    BouncingBall(root)
    root.mainloop()

if __name__ == "__main__":
    main()

