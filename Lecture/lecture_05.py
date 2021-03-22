# Surface
import pygame

pygame.init()
#size of screnn
W = 600
H = 400
#screen
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Surface")
#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock() # for FPS

surf = pygame.Surface((W, 200))
bita = pygame.Surface((50, 10))

surf.fill(BLUE)
bita.fill(RED)

# for surf
x, y = 0, 0
# for bita
bx, by = 0, 150

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.fill(BLUE)
    # drawing bita in the surf surface
    surf.blit(bita, (bx, by))
    if bx < W:
        bx += 5
    else:
        bx = 0

    if y < H:
        y += 1
    else:
        y = 0
    screen.fill(WHITE)
    screen.blit(surf, (x, y))
    pygame.display.update()

    clock.tick(FPS)