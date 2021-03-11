import pygame

pygame.init() # imprtit 

# RESIZABLE - window with variable parameters
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)

#set caption  
pygame.display.set_caption("New Game")
# set images of your game 
pygame.display.set_icon(pygame.image.load("doggie-bmp.png"))

FPS = 60

clock = pygame.time.Clock()

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			run = False

	clock.tick(FPS)

print("program is ended")
