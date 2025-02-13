import pygame
import sys

# Initialize pygame
pygame.init()

# Get the screen size
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Create a fullscreen window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Fill the screen with black
screen.fill((0, 0, 0))
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False
        elif event.type == pygame.KEYDOWN:
            running = False

# Quit pygame and exit the script
pygame.quit()
sys.exit()