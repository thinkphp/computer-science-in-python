import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Graphics Demo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)  # Color for hexagon

# Animation variables
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
angle = 0

# Hexagon parameters
hex_center_x = 600
hex_center_y = 100
hex_radius = 50
hex_points = []

# Calculate hexagon vertices
for i in range(6):
    # 2π/6 = 60 degrees in radians
    angle_hex = i * 2 * math.pi / 6
    x = hex_center_x + hex_radius * math.cos(angle_hex)
    y = hex_center_y + hex_radius * math.sin(angle_hex)
    hex_points.append((x, y))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Draw static shapes
    # Rectangle
    pygame.draw.rect(screen, RED, (50, 50, 100, 80))

    # Triangle
    pygame.draw.polygon(screen, GREEN, [(200, 50), (300, 50), (250, 150)])

    # Line
    pygame.draw.line(screen, BLACK, (350, 50), (450, 150), 5)

    # Hexagon
    pygame.draw.polygon(screen, PURPLE, hex_points)

    # Animated circle
    # Make circle move in a circular pattern
    circle_x = WIDTH // 2 + math.cos(angle) * 100

    circle_y = HEIGHT // 2 + math.sin(angle) * 100

    pygame.draw.circle(screen, BLUE, (int(circle_x), int(circle_y)), 30)

    # Update angle for animation
    angle += 0.02

    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Pygame Graphics", True, BLACK)
    screen.blit(text, (WIDTH // 2 - 100, 50))

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
