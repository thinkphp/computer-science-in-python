import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Orbit Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)  # Sun color
BLUE = (0, 0, 255)      # Planet color

# Orbit parameters
sun_x = WIDTH // 2
sun_y = HEIGHT // 2
orbit_radius_x = 200  # Horizontal radius (semi-major axis)
orbit_radius_y = 100  # Vertical radius (semi-minor axis)
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
    screen.fill(BLACK)

    # Draw the sun (center of the orbit)
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), 40)

    # Calculate the planet's position in the elliptical orbit
    planet_x = sun_x + math.cos(angle) * orbit_radius_x
    planet_y = sun_y + math.sin(angle) * orbit_radius_y

    # Draw the planet
    pygame.draw.circle(screen, BLUE, (int(planet_x), int(planet_y)), 20)

    # Update the angle for the orbit
    angle += 0.02  # Adjust this value to change orbit speed

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
