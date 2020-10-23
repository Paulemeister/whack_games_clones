import pygame

grid_size_x = 16*5
grid_size_y = 9*5
grid_width = 20
width = (grid_size_x+1)*grid_width
height = (grid_size_y+1)*grid_width
pygame.init()
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
cube_size = 0.8
array = []
running = True
last_key = 0

def to_screen(coord):
	result = (coord+0.5)*grid_width
	return result

class Snake:
	def __init__(self,lenght,x,y):
		self.lenght = lenght
		self.position = [x,y]
		self.x = x
		self.y = y
		self.rectangles = []
		for i in range(lenght,0,-1):
			print(i)
			x = to_screen(self.position[0])
			y = to_screen(self.position[1]+-1)
			rect = pygame.Rect(x,y,grid_width*cube_size,grid_width*cube_size)
			rect.center = [x,y]
			self.rectangles.append(rect)
		for rect in self.rectangles:
			pygame.draw.rect(screen,(255,0,0),rect)
	def move(self,x_new,y_new):
		print("move to {} {}".format(x_new,y_new))
		print(self.rectangles)
		pygame.draw.rect(screen,(0,0,0),self.rectangles[0])
		del self.rectangles[0]
		x = to_screen(x_new)
		y = to_screen(y_new)
		rect =  pygame.Rect(x,y,grid_width*cube_size,grid_width*cube_size)
		rect.center = [x,y]
		self.rectangles.append(rect)
		pygame.draw.rect(screen,(255,0,0),rect)
		print(self.rectangles)
		self.x = x_new
		self.y = y_new
		self.position = [x_new,y_new]


snake = Snake(5,0,0)
new_x = new_y = 0
x=y=0
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			
			if (event.key == pygame.K_w) & (last_key != pygame.K_s):
				new_x = 0
				new_y = -1
			if (event.key == pygame.K_s) & (last_key != pygame.K_w):
				new_x = 0
				new_y = 1
			if (event.key == pygame.K_d) & (last_key != pygame.K_a):
				new_x = 1
				new_y = 0
			if (event.key == pygame.K_a) & (last_key != pygame.K_d):
				new_x = -1
				new_y = 0
			last_key = event.key

	x = snake.x + new_x
	y = snake.y + new_y
	if y > grid_size_y:
		y = 0
	elif y < 0:
		y = grid_size_y

	if x > grid_size_x:
		x = 0
	elif x < 0:
		x = grid_size_x
	snake.move(x,y)			
	pygame.display.update()
	clock.tick(10)