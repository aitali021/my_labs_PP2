import pygame
import random
import sys
import os
import time




pygame.init()
en = 600
uzyndyq = 400
olshem = 20
kok = (0, 150, 255)
qyzyl = (255, 0, 0)
aq = (255, 255, 255)
screen = pygame.display.set_mode((en, uzyndyq))
pygame.display.set_caption("Snake Game")
arty = pygame.image.load(os.path.join("images", "bgjpg.jpg"))
arty = pygame.transform.scale(arty, (en, uzyndyq))
clock = pygame.time.Clock()
jylan_speed = 10
jylan = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
score = 0
level = 1



def generate_food():
    while True:
        x = random.randrange(0, en, olshem)
        y = random.randrange(0, uzyndyq, olshem)
        if (x, y) not in jylan:
            weight = random.randint(1, 3)  #random weight for food
            return (x, y, weight)
#generate food with random weights

alma_orny = generate_food() #create food



font = pygame.font.SysFont(None, 30)
def draw_text(text, x, y, color=aq):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))
#draw text (score, level)



running = True
food_creation_time = time.time()
while running:
    screen.blit(arty, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    head_x, head_y = jylan[0]
    if direction == "UP":
        head_y -= olshem
    elif direction == "DOWN":
        head_y += olshem
    elif direction == "LEFT":
        head_x -= olshem
    elif direction == "RIGHT":
        head_x += olshem

    new_head = (head_x, head_y)
    # Main game loop
    if head_x < 0 or head_x >= en or head_y < 0 or head_y >= uzyndyq or new_head in jylan:
        running = False
    jylan.insert(0, new_head)
    #add new head and checking



    #check if snake eats food
    if new_head == alma_orny[:2]:
        score += alma_orny[2]  #add food weight to score
        if score % 3 == 0:
            level += 1
            jylan_speed += 2
        alma_orny = generate_food()

    else:
        jylan.pop()  #remove tail

    pygame.draw.rect(screen, qyzyl, (alma_orny[0], alma_orny[1], olshem, olshem))
    #draw food
    

    for segment in jylan:
        pygame.draw.rect(screen, kok, (segment[0], segment[1], olshem, olshem))
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Level: {level}", 10, 30)
    #draw snake


    if time.time() - food_creation_time > 5:
        alma_orny = generate_food()
        food_creation_time = time.time()
    #check if food is expired (disappears after 5 seconds)
    pygame.display.update()
    clock.tick(jylan_speed)

pygame.quit()
sys.exit()
