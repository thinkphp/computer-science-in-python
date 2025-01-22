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

# Animation variables
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
angle = 0

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
