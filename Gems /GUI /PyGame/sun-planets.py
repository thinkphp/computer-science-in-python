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
BLUE = (0, 0, 255)      # First planet color
RED = (255, 0, 0)       # Second planet color
LIGHT_BLUE = (100, 100, 255)  # First orbit path color
LIGHT_RED = (255, 100, 100)   # Second orbit path color

# Orbit parameters
sun_x = WIDTH // 2
sun_y = HEIGHT // 2

# First planet parameters
orbit_radius_x1 = 200  # Horizontal radius (semi-major axis)
orbit_radius_y1 = 100  # Vertical radius (semi-minor axis)
angle1 = 0

# Second planet parameters
orbit_radius_x2 = 300  # Larger orbit
orbit_radius_y2 = 150  # Larger orbit
angle2 = 0

# Function to draw elliptical orbit
def draw_orbit(surface, color, center_x, center_y, radius_x, radius_y):
    points = []
    for i in range(360):
        angle = math.radians(i)
        x = center_x + math.cos(angle) * radius_x
        y = center_y + math.sin(angle) * radius_y
        points.append((int(x), int(y)))
    pygame.draw.lines(surface, color, True, points, 1)

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

    # Draw orbit paths
    draw_orbit(screen, LIGHT_BLUE, sun_x, sun_y, orbit_radius_x1, orbit_radius_y1)
    draw_orbit(screen, LIGHT_RED, sun_x, sun_y, orbit_radius_x2, orbit_radius_y2)

    # Draw the sun (center of the orbit)
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), 40)

    # Calculate and draw first planet (blue)
    planet_x1 = sun_x + math.cos(angle1) * orbit_radius_x1
    planet_y1 = sun_y + math.sin(angle1) * orbit_radius_y1
    pygame.draw.circle(screen, BLUE, (int(planet_x1), int(planet_y1)), 20)

    # Calculate and draw second planet (red)
    planet_x2 = sun_x + math.cos(angle2) * orbit_radius_x2
    planet_y2 = sun_y + math.sin(angle2) * orbit_radius_y2
    pygame.draw.circle(screen, RED, (int(planet_x2), int(planet_y2)), 25)

    # Update the angles for the orbits
    angle1 += 0.02  # First planet speed
    angle2 += 0.015  # Second planet speed (slightly slower)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
