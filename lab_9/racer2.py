import pygame
import random
import os



pygame.init()
en, uzyndyq = 400, 600
screen = pygame.display.set_mode((en, uzyndyq))
pygame.display.set_caption("Car Racer")
clock = pygame.time.Clock()
FPS = 60
IMG_DIR = os.path.join("images")
jol = pygame.image.load(os.path.join(IMG_DIR, "jol.jpg"))
jol = pygame.transform.scale(jol, (en, uzyndyq))
car = pygame.image.load(os.path.join(IMG_DIR, "car.png"))
car = pygame.transform.scale(car, (50, 100))
enemy = pygame.image.load(os.path.join(IMG_DIR, "enemy.png"))
enemy = pygame.transform.scale(enemy, (50, 100))
coin_img = pygame.image.load(os.path.join(IMG_DIR, "coin.png"))
coin_img = pygame.transform.scale(coin_img, (40, 40))
font = pygame.font.SysFont("Arial", 30)
bg_y = 0
score = 0
coin_weight = 1
enemy_speed_increase = 1 
#increase enemy speed when coins are collected


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car
        self.rect = self.image.get_rect()
        self.rect.center = (en // 2, uzyndyq - 120)
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < en:
            self.rect.x += self.speed
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(40, en - 90)
        self.rect.y = -100
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > uzyndyq:
            self.rect.x = random.randint(40, en - 90)
            self.rect.y = -100
class Coin(pygame.sprite.Sprite):
    def __init__(self, weight):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, en - 70)
        self.rect.y = -50
        self.weight = weight
        self.speed = 4
        #random weight to each coin


    def update(self):
        self.rect.y += self.speed
        if self.rect.top > uzyndyq:
            self.kill()

# Game setup
player = Player()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create first enemy
enemy = Enemy(5)
enemies.add(enemy)
all_sprites.add(enemy)

COIN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_EVENT, 1500)

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == COIN_EVENT:
            coin = Coin(random.randint(1, 3))  #random weight for each coin
            coins.add(coin)
            all_sprites.add(coin)

    bg_y += 5
    if bg_y >= uzyndyq:
        bg_y = 0
    all_sprites.update()

    collected = pygame.sprite.spritecollide(player, coins, True)
    score += sum([coin.weight for coin in collected])
    #add the weight of each collected coin



    if score >= 10:
        enemy.speed += enemy_speed_increase
    if pygame.sprite.spritecollide(player, enemies, False):
        running = False
    #increase enemy speed after collecting 10 coins

    screen.blit(jol, (0, bg_y - uzyndyq))
    screen.blit(jol, (0, bg_y))
    all_sprites.draw(screen)
    text = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()
