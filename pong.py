# assignment
"""
1. screen size 240x240
2. create a ball of size 10 in the middle
3. make red ball move left,right,up,down with the arrow keys
4. keep the ball inside the screen
5. can you change the ball size or screen width and height easily just by changing the variables?
6. can you make the ball move while you hold down each arrow key?
"""

import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# settings
screen_width = 240
screen_height = 240
ball_size = 20 # diameter
ball_step = 20

# Screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('assignment')

# Colors
ball_color = (255,0,0)
bg_color = pygame.Color('grey10')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2, ball_size, ball_size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				ball.y -= ball_step
			if event.key == pygame.K_DOWN:
				ball.y += ball_step
			if event.key == pygame.K_LEFT:
				ball.x -= ball_step
			if event.key == pygame.K_RIGHT:
				ball.x += ball_step

	
	if ball.top <= 0:
		ball.top = 0
	if ball.bottom >= screen_height:
		ball.bottom = screen_height
	if ball.left <= 0:
		ball.left = 0
	if ball.right >= screen_width:
		ball.right = screen_width

	# Visuals 
	screen.fill(bg_color)
	pygame.draw.ellipse(screen, ball_color, ball)




	pygame.display.flip()
	clock.tick(60)