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
# flag about starting drawing
flStartDraw = False
#sp --> start drawing, ep --> end drawing
sp=ep=None

screen.fill(WHITE)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # start of drawing
            flStartDraw = True
            # get inf about position of cursor
            sp = event.pos
        # position of mouse
        elif event.type == pygame.MOUSEMOTION:
            if flStartDraw:
                pos = event.pos

                width = pos[0] - sp[0]
                height = pos[1] - sp[1]

                screen.fill(WHITE)
                pygame.draw.rect(screen, RED, (sp[0], sp[1], width, height))
                pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                flStartDraw = False




clock.tick(FPS)
