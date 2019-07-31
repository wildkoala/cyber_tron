import pygame

pygame.init()

# Create the screen
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CYBER TRON")


# player global variables
# (x,y) are the coordinates of the top left corner of the player
x = 495
y = 495
player_width = 10
player_height = 10
speed = 5



# Store the instances of players?
# players = [Player("Twiggy", Player("Ryan")]


# GAME LOOP
run = True
while run:

		# Set the screen refresh rate in milliseconds.
		pygame.time.delay(40)

		# Graceful Exit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# Handle keys getting pressed by users
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			x -= speed
		if keys[pygame.K_RIGHT]:
			x += speed
		if keys[pygame.K_UP]:
			y -= speed
		if keys[pygame.K_DOWN]:
			y += speed

		# Handle collisions with the walls - currently causes the game to exit.
		if x < 0:
			print("COLLIDED WITH LEFT WALL")
			run = False
		if x > width - player_width:
			print("COLLIDED WITH RIGHT WALL")
			run = False
		if y < 0:
			print("COLLIDED WITH UPPER WALL")
			run = False
		if y > height - player_height:
			print("COLLIDED WITH LOWER WALL")
			run = False
		
		# Handle collisions with the walls - currently causes the game to exit.

		pygame.draw.rect(screen, (255, 0 ,255), (x, y, player_width, player_height))
		pygame.display.update()

pygame.quit()








# Classes - NOT YET IN USE


class Block:
	def __init__(self, color, size):
		self.color = color
		self.size = size # in terms of pixels

class Board:
	def __init__(self, num_of_players, size):
		self.num_of_players = num_of_players
		self.size = size #in terms of blocks




class Player: #give board obj for board.
	def __init__(self,color, location, direction, board):
		self.color = color
		self.is_alive = True
		self.location = location
		self.direction = direction
		self.board = board

	def dies (self):
		self.is_alive = False




