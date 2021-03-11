# обработка событий 
import pygame 

pygame.init()

W = 600
H = 400

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("keyboard events")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock() # for FPS

# х, y -> начальное положение прямоугольника на экране 
# x, y -> the initial position of the rectangle on the screen

x = W // 2
y = H // 2
speed = 4
move = 0

run = True
while run: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		# first method (with one another key together) (with shift)
		elif event.type == pygame.KEYDOWN: # if pressed
			# if pressed left key with shift
			if event.key == pygame.K_LEFT and event.key == pygame.KMOD_LSHIFT:
				move -= speed 
			# if pressed right key with shift
			elif event.key == pygame.K_RIGHT and event.key == pygame.KMOD_LSHIFT:
				move = speed

		elif event.type == pygame.KEYUP: # отжатие 
			if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
				move = 0



	# second method 
	keys = pygame.key.get_pressed() # фннкция для получения индекса нажатой кнопки

	if keys[pygame.K_LEFT]:
		x -= speed
	elif keys[pygame.K_RIGHT]:
		x += speed



	screen.fill(WHITE) # paint over 
	pygame.draw.rect(screen, BLUE, (x, y, 10, 20))
	pygame.display.update()

	clock.tick(FPS)



