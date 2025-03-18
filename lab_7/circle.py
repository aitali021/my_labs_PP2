import pygame
import sys



pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dopty kozgalt")
white = (255, 255, 255)
red = (150, 0, 0)
ball_radius = 15
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < screen_height:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < screen_width:
        ball_x += ball_speed
    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(30)
pygame.quit()
sys.exit()
