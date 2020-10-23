import pygame

grid_size_x = 16*5
grid_size_y = 9*5
grid_width = 20
width = (grid_size_x+1)*grid_width
height = (grid_size_y+1)*grid_width
pygame.init()
screen = pygame.display.set_mode([width, height])

cube_size = 0.1
array = []
running = True

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
			y = to_screen(self.position[1]+i-1)
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
snake2 = Snake(10,5,5)
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				new_x = snake.x
				new_y = snake.y-1
			if event.key == pygame.K_s:
				new_x = snake.x
				new_y = snake.y+1
			if event.key == pygame.K_d:
				new_x = snake.x+1
				new_y = snake.y
			if event.key == pygame.K_a:
				new_x = snake.x-1
				new_y = snake.y

			if new_y > grid_size_y:
				new_y = 0
			elif new_y < 0:
				new_y = grid_size_y

			if new_x > grid_size_x:
				new_x = 0
			elif new_x < 0:
				new_x = grid_size_x
			snake.move(new_x,new_y)
				
	pygame.display.update()