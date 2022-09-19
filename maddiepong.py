#from curses import KEY_DOWN
import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
backgroundcolor = pygame.Color(49, 51, 49)
screen = pygame.display.set_mode((screen_width, screen_height))

ballsize = 20
ballcolour = pygame.Color(166, 224, 177)
ball = pygame.Rect(screen_width / 2 - ballsize / 2, screen_height / 2 - ballsize / 2, ballsize, ballsize)
ballx_speed = 2
bally_speed = 2

player_gap = 30
player_width = 20
player_height = 120
player_color = pygame.Color("white")
player1 = pygame.Rect(player_gap, screen_height / 2 - player_height / 2, player_width, player_height)
player2 = pygame.Rect(screen_width - player_gap - player_width, screen_height / 2 - player_height / 2, player_width, player_height)
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            print("key is pressed down")
            if event.key == pygame.K_UP:
                player_speed -= 4
            if event.key == pygame.K_DOWN:
                player_speed += 4
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_UP:
                player_speed += 4
            if event.key == pygame.K_DOWN:
                player_speed -= 4
            print("key is pressed up")           

    screen.fill(backgroundcolor)
    pygame.draw.ellipse(screen, ballcolour, ball)
    pygame.draw.rect(screen, player_color, player1)
    pygame.draw.rect(screen, player_color, player2)
    
    # ball animation
    ball.x += ballx_speed
    ball.y += bally_speed
    if ball.bottom >= screen_height or ball.top <= 0:
        bally_speed *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ballx_speed *= -1

    #make the ball bounce from player1
    if ball.colliderect(player1):
        ballx_speed *= -1

    # player animation
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
        #player_speed = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height
        #player_speed = 0
    print("player speed", player_speed)


    pygame.display.flip()        
    clock.tick (60)