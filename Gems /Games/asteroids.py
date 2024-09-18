import tkinter as tk
import random
import math

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF0000"

# Utility functions
def wrap_position(position, width, height):
    """Wrap objects around screen edges."""
    x, y = position
    return [x % width, y % height]

def distance(p1, p2):
    """Calculate distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Game objects
class GameObject:
    def __init__(self, canvas, position, velocity, size):
        self.canvas = canvas
        self.position = list(position)
        self.velocity = list(velocity)
        self.size = size
        self.shape = None

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position = wrap_position(self.position, WIDTH, HEIGHT)

    def draw(self):
        pass

class Spaceship(GameObject):
    def __init__(self, canvas):
        super().__init__(canvas, [WIDTH // 2, HEIGHT // 2], [0, 0], 20)
        self.angle = 0
        self.thrust_power = 0.2
        self.rotation_speed = 5
        self.bullets = []
        self.shoot_delay = 250
        self.last_shot = 0
        self.is_thrusting = False
        self.is_rotating_left = False
        self.is_rotating_right = False

    def rotate(self, direction):
        self.angle += direction * self.rotation_speed
        self.angle %= 360

    def thrust(self):
        angle_rad = math.radians(self.angle)
        self.velocity[0] += math.cos(angle_rad) * self.thrust_power
        self.velocity[1] += math.sin(angle_rad) * self.thrust_power

    def shoot(self):
        now = self.canvas.winfo_toplevel().tk.call('clock', 'milliseconds')
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.canvas, list(self.position), self.angle)
            self.bullets.append(bullet)

    def update(self):
        if self.is_rotating_left:
            self.rotate(-1)
        if self.is_rotating_right:
            self.rotate(1)
        if self.is_thrusting:
            self.thrust()

        super().update()
        self.velocity[0] *= 0.98
        self.velocity[1] *= 0.98

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def draw(self):
        if self.shape:
            self.canvas.delete(self.shape)

        angle_rad = math.radians(self.angle)
        tip = (self.position[0] + math.cos(angle_rad) * self.size,
               self.position[1] + math.sin(angle_rad) * self.size)
        left_corner = (self.position[0] + math.cos(angle_rad + 2.5) * self.size,
                       self.position[1] + math.sin(angle_rad + 2.5) * self.size)
        right_corner = (self.position[0] + math.cos(angle_rad - 2.5) * self.size,
                        self.position[1] + math.sin(angle_rad - 2.5) * self.size)

        self.shape = self.canvas.create_polygon(tip, left_corner, right_corner, fill=WHITE)

        for bullet in self.bullets:
            bullet.draw()

class Bullet(GameObject):
    def __init__(self, canvas, position, angle):
        speed = 10
        velocity = [math.cos(math.radians(angle)) * speed,
                    math.sin(math.radians(angle)) * speed]
        super().__init__(canvas, position, velocity, 3)
        self.lifetime = 60  # frames

    def update(self):
        super().update()
        self.lifetime -= 1

    def draw(self):
        if self.shape:
            self.canvas.delete(self.shape)
        self.shape = self.canvas.create_oval(self.position[0] - self.size, self.position[1] - self.size,
                                             self.position[0] + self.size, self.position[1] + self.size,
                                             fill=WHITE)

    def off_screen(self):
        return (self.lifetime <= 0 or
                self.position[0] < 0 or self.position[0] > WIDTH or
                self.position[1] < 0 or self.position[1] > HEIGHT)

class Asteroid(GameObject):
    def __init__(self, canvas, size=None):
        if size is None:
            size = random.randint(30, 50)
        position = self.get_spawn_position(size)
        velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]
        super().__init__(canvas, position, velocity, size)
        self.rotation = 0
        self.rotation_speed = random.uniform(-3, 3)

    def get_spawn_position(self, size):
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            return [random.randint(0, WIDTH), -size]
        elif side == 'bottom':
            return [random.randint(0, WIDTH), HEIGHT + size]
        elif side == 'left':
            return [-size, random.randint(0, HEIGHT)]
        else:  # right
            return [WIDTH + size, random.randint(0, HEIGHT)]

    def update(self):
        super().update()
        self.rotation += self.rotation_speed

    def draw(self):
        if self.shape:
            self.canvas.delete(self.shape)

        points = []
        for i in range(8):
            angle = math.radians(self.rotation + i * 45)
            points.extend([
                self.position[0] + math.cos(angle) * self.size,
                self.position[1] + math.sin(angle) * self.size
            ])

        self.shape = self.canvas.create_polygon(points, outline=WHITE, fill='')

    def split(self):
        if self.size > 15:
            return [Asteroid(self.canvas, self.size // 2) for _ in range(2)]
        return []

class Game:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg=BLACK)
        self.canvas.pack()

        self.spaceship = Spaceship(self.canvas)
        self.asteroids = [Asteroid(self.canvas) for _ in range(5)]
        self.score = 0
        self.score_display = self.canvas.create_text(10, 10, anchor="nw", fill=WHITE, text="Score: 0")
        self.debug_info = self.canvas.create_text(10, 30, anchor="nw", fill=WHITE, text="")

        self.bind_keys()
        self.update()

    def bind_keys(self):
        self.master.bind("<KeyPress-Left>", lambda e: setattr(self.spaceship, 'is_rotating_left', True))
        self.master.bind("<KeyRelease-Left>", lambda e: setattr(self.spaceship, 'is_rotating_left', False))
        self.master.bind("<KeyPress-Right>", lambda e: setattr(self.spaceship, 'is_rotating_right', True))
        self.master.bind("<KeyRelease-Right>", lambda e: setattr(self.spaceship, 'is_rotating_right', False))
        self.master.bind("<KeyPress-Up>", lambda e: setattr(self.spaceship, 'is_thrusting', True))
        self.master.bind("<KeyRelease-Up>", lambda e: setattr(self.spaceship, 'is_thrusting', False))
        self.master.bind("<space>", lambda e: self.spaceship.shoot())

    def handle_collisions(self):
        for asteroid in self.asteroids[:]:
            if distance(self.spaceship.position, asteroid.position) < asteroid.size + self.spaceship.size:
                return True  # Game over

            for bullet in self.spaceship.bullets[:]:
                if distance(bullet.position, asteroid.position) < asteroid.size:
                    self.spaceship.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    self.asteroids.extend(asteroid.split())
                    self.score += 100
                    self.canvas.itemconfigure(self.score_display, text=f"Score: {self.score}")
                    break

        return False

    def update(self):
        self.canvas.delete("all")
        self.score_display = self.canvas.create_text(10, 10, anchor="nw", fill=WHITE, text=f"Score: {self.score}")

        self.spaceship.update()
        self.spaceship.draw()

        for asteroid in self.asteroids:
            asteroid.update()
            asteroid.draw()

        if self.handle_collisions():
            self.game_over()
            return

        if len(self.asteroids) < 5:
            self.asteroids.append(Asteroid(self.canvas))

        # Debug info
        debug_text = f"Ship: pos={self.spaceship.position}, vel={self.spaceship.velocity}, angle={self.spaceship.angle}"
        self.debug_info = self.canvas.create_text(10, 30, anchor="nw", fill=WHITE, text=debug_text)

        self.master.after(int(1000 / FPS), self.update)

    def game_over(self):
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER", fill=RED, font=("Arial", 32))

def main():
    root = tk.Tk()
    root.title("Asteroids")
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()
