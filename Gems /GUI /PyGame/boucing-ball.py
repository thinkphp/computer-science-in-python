import pygame
import sys
import math  # Add this import for sin function

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Walking Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
BALL_RADIUS = 20
ball_x = WIDTH // 2
ball_y = HEIGHT - BALL_RADIUS  # Place ball at bottom of screen
ball_speed = 5
direction = 1  # 1 for right, -1 for left

# Animation properties for bouncing effect
bounce_height = 10
bounce_speed = 0.1
bounce_offset = 0
bounce_time = 0

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update ball position
    ball_x += ball_speed * direction
    
    # Change direction when hitting screen edges
    if ball_x >= WIDTH - BALL_RADIUS:
        direction = -1  # Move left
    elif ball_x <= BALL_RADIUS:
        direction = 1   # Move right
    
    # Create bouncing motion using math.sin instead of pygame.math.sin
    bounce_time += bounce_speed
    bounce_offset = abs(bounce_height * math.sin(bounce_time))
    current_y = ball_y - bounce_offset
    
    # Clear screen
    screen.fill(WHITE)
    
    # Draw shadow (optional, makes it look more realistic)
    shadow_radius = max(5, BALL_RADIUS - bounce_offset/2)
    pygame.draw.ellipse(screen, (200, 200, 200), 
                       (ball_x - shadow_radius, HEIGHT - BALL_RADIUS/2, 
                        shadow_radius*2, BALL_RADIUS/2))
    
    # Draw ball with bounce effect
    pygame.draw.circle(screen, RED, (int(ball_x), int(current_y)), BALL_RADIUS)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
