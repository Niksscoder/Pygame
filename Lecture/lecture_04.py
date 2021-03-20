# keyboard events
import pygame

# methods of this lecture
# pygame.MOUSEBUTTONDOWN – mouse click down;
# pygame.MOUSEBUTTONUP – mouse click up;
# pygame.MOUSEMOTION – moving the mouse cursor;
# pygame.MOUSEWHEEL – mouse wheel rotation.(вращение)

pygame.init()
#size of screnn
W = 600
H = 400
#screen
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("mouse events")
#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock() # for FPS
# for drawing some figures
# if sp == None: for this case we don't draw rect yet
# else --> draw
sp = None

screen.fill(WHITE)
pygame.display.update()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        pressed = pygame.mouse.get_pressed()
        # [0] index means that clicked down on the left button
        if pressed[0]:
            # return set of coordinates
            pos = pygame.mouse.get_pos()

            if sp is None:
                # if we haven't started drawing yet -->
                # sp ==pos(start position)
                sp = pos
            width = pos[0] - sp[0]
            height = pos[1] - sp[1]

            screen.fill(WHITE)
            pygame.draw.rect(screen, RED, (sp[0], sp[1], width, height))
            pygame.display.update()
        else:
            sp = None







    clock.tick(FPS)
