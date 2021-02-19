# Pygame skeleton template for a new Pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 480
# FPD for updating
FPS = 30

# colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create game and display
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# loop of the game
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Updating

    # Rendering
    screen.fill(BLACK)
    # and flip display
    pygame.display.flip()

pygame.quit()
