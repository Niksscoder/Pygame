import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Class Rect")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()


ground = H - 70  # ground level
jump_force = 20  # jump power
move = jump_force + 1

# our hero
hero = pygame.Surface((40, 50))
hero.fill(BLUE) # color is blue
rect = hero.get_rect(centerx=W // 2) # will be at the centre of the screen
rect.bottom = ground # put it at ground lvl

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            # if pressed space buttom and "hero" stay on the ground at this moment
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                # in this case our "hero" jump
                move = -jump_force

    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force + 1

    sc.fill(WHITE)
    sc.blit(hero, rect)
    pygame.display.update()

    clock.tick(FPS)