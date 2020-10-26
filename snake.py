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

def init():
	row = []
	for j in range(grid_size_y):
		row.append([])
	for i in range(grid_size_x):
		array.append(row)

def to_screen(coord):
	return (coord+0.5)*grid_width

class Snake:
	def __init__(self,lenght,color,x,y):
		self.lenght = lenght
		self.position = [x,y]
		self.x = x
		self.y = y
		self.rectangles = []
		self.rectangles_pos = []
		self.color = color
		self.collided = False
		for i in range(lenght,0,-1):
			x = to_screen(self.position[0])
			y = to_screen(self.position[1]+-1)
			rect = pygame.Rect(x,y,grid_width*cube_size,grid_width*cube_size)
			rect.center = [x,y]
			self.rectangles.append(rect)
			self.rectangles_pos.append((self.x,self.y))
		for rect in self.rectangles:
			pygame.draw.rect(screen,self.color,rect)

	def move(self,x_new,y_new):
		print("move to {} {}".format(x_new,y_new))
		for pos in self.rectangles_pos:
			if pos == (x_new,y_new):
				self.collided = True
		if self.collided:
			for i in range(self.lenght-1):
				pygame.draw.rect(screen,(0,0,0),self.rectangles[i])
			self.rectangles = [self.rectangles[self.lenght-1]]
			self.rectangles_pos = [self.rectangles_pos[self.lenght-1]]
			self.add_lenght(5)
			self.lenght = 1
			self.collided = False

		print(self.rectangles_pos)
		pygame.draw.rect(screen,(0,0,0),self.rectangles[0])
		del self.rectangles[0]
		del self.rectangles_pos[0]
		x = to_screen(x_new)
		y = to_screen(y_new)
		rect =  pygame.Rect(x,y,grid_width*cube_size,grid_width*cube_size)
		rect.center = [x,y]
		self.rectangles.append(rect)
		self.rectangles_pos.append((x_new,y_new))
		pygame.draw.rect(screen,self.color,rect)
		print(self.rectangles_pos)
		self.x = x_new
		self.y = y_new
		self.position = [x_new,y_new]

	def add_lenght(self,add):
		for i in range(add):
			self.rectangles.insert(0,self.rectangles[0])
			self.rectangles_pos.insert(0,self.rectangles_pos[0])
		self.lenght += add

init()
for i in array:
	print(i)
snake = Snake(5,(255,255,0),0,0)
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
			if event.key == pygame.K_SPACE:
				snake.add_lenght(1)
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