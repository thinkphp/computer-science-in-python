import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
MAGNET_WIDTH = 100
MAGNET_HEIGHT = 50
MAGNET_LEG_WIDTH = 20
EGG_WIDTH = 30  # Oval shape
EGG_HEIGHT = 40  # Oval shape
MAGNET_SPEED = 20
EGG_SPEED = 5
LIVES = 3

class EggCatcherGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Egg Catcher Game - Magnet")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightblue")
        self.canvas.pack()

        # Magnet (U-shaped facing downwards, legs up)
        self.magnet = self.draw_magnet(WINDOW_WIDTH//2 - MAGNET_WIDTH//2, WINDOW_HEIGHT - MAGNET_HEIGHT - 10)

        # Lives and score
        self.lives = LIVES
        self.score = 0
        self.lives_display = self.canvas.create_text(50, 20, text=f"Lives: {self.lives}", fill="black", font=('Helvetica', 14))
        self.score_display = self.canvas.create_text(WINDOW_WIDTH - 50, 20, text=f"Score: {self.score}", fill="black", font=('Helvetica', 14))

        # List to store falling eggs
        self.eggs = []

        # Bind keys
        self.root.bind("<Left>", self.move_magnet_left)
        self.root.bind("<Right>", self.move_magnet_right)

        # Start the game
        self.spawn_egg()
        self.update_game()

    def draw_magnet(self, x, y):
        """Draw a downward-facing U-shaped magnet with legs up"""
        # Left leg of the U
        left_leg = self.canvas.create_rectangle(x, y, x + MAGNET_LEG_WIDTH, y + MAGNET_HEIGHT, fill="red")
        # Right leg of the U
        right_leg = self.canvas.create_rectangle(x + MAGNET_WIDTH - MAGNET_LEG_WIDTH, y,
                                                 x + MAGNET_WIDTH, y + MAGNET_HEIGHT, fill="red")
        # Bottom bar of the U (connecting legs)
        bottom_bar = self.canvas.create_rectangle(x + MAGNET_LEG_WIDTH, y + MAGNET_HEIGHT - MAGNET_LEG_WIDTH,
                                                  x + MAGNET_WIDTH - MAGNET_LEG_WIDTH, y + MAGNET_HEIGHT, fill="red")
        return left_leg, right_leg, bottom_bar

    def move_magnet_left(self, event):
        if self.canvas.coords(self.magnet[0])[0] > 0:
            for part in self.magnet:
                self.canvas.move(part, -MAGNET_SPEED, 0)

    def move_magnet_right(self, event):
        if self.canvas.coords(self.magnet[1])[2] < WINDOW_WIDTH:
            for part in self.magnet:
                self.canvas.move(part, MAGNET_SPEED, 0)

    def spawn_egg(self):
        # Spawn a new egg at a random x position
        x = random.randint(10, WINDOW_WIDTH - EGG_WIDTH - 10)
        # Generate random color for the egg
        random_color = random.choice(["red", "blue", "green", "purple", "orange", "pink", "yellow"])
        # Create an oval-shaped egg
        egg = self.canvas.create_oval(x, 0, x + EGG_WIDTH, EGG_HEIGHT, fill=random_color)
        self.eggs.append(egg)
        # Spawn eggs at regular intervals
        self.root.after(2000, self.spawn_egg)

    def update_game(self):
        # Move each egg down
        for egg in self.eggs[:]:
            self.canvas.move(egg, 0, EGG_SPEED)
            egg_coords = self.canvas.coords(egg)

            # Check if egg is caught
            if self.check_caught(egg_coords):
                self.eggs.remove(egg)
                self.canvas.delete(egg)
                self.score += 1
                self.update_score()

            # Check if egg hits the bottom
            elif egg_coords[3] >= WINDOW_HEIGHT:
                self.eggs.remove(egg)
                self.canvas.delete(egg)
                self.lives -= 1
                self.update_lives()
                if self.lives <= 0:
                    self.game_over()
                    return

        # Continue game loop
        self.root.after(50, self.update_game)

    def check_caught(self, egg_coords):
        # Get the coordinates of the magnet legs
        magnet_coords_left_leg = self.canvas.coords(self.magnet[0])
        magnet_coords_right_leg = self.canvas.coords(self.magnet[1])

        # Check if the egg is within the bounds of the magnet's legs
        if (magnet_coords_left_leg[0] < egg_coords[2] and  # Left boundary of egg inside left leg
            magnet_coords_right_leg[2] > egg_coords[0] and  # Right boundary of egg inside right leg
            egg_coords[1] <= magnet_coords_left_leg[3] and  # Egg top touches magnet legs
            egg_coords[3] > magnet_coords_left_leg[1]):     # Egg passes between the legs
            return True
        return False

    def update_score(self):
        self.canvas.itemconfig(self.score_display, text=f"Score: {self.score}")

    def update_lives(self):
        self.canvas.itemconfig(self.lives_display, text=f"Lives: {self.lives}")

    def game_over(self):
        self.canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text="Game Over", fill="red", font=('Helvetica', 24))
        self.root.after(2000, self.root.quit)

# Create the game window and start the game
root = tk.Tk()
game = EggCatcherGame(root)
root.mainloop()
