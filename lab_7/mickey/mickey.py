import pygame
import time



pygame.init()
sagat = pygame.image.load(r"C:\Users\Aitali\Documents\new folder\labs\lab_7\mickey\mickeyclock.jpeg")
on_kol = pygame.image.load(r"C:\Users\Aitali\Documents\new folder\labs\lab_7\mickey\onkool.png")
sol_kol = pygame.image.load(r"C:\Users\Aitali\Documents\new folder\labs\lab_7\mickey\photosolkolulken.png")
rct = sagat.get_rect()
screen = pygame.display.set_mode((rct.width, rct.height))
pygame.display.set_caption("Mickey Clock")
def rotate_hand(qwww, angle, ee, hand_offset):
    rotated_surface = pygame.transform.rotate(qwww, angle)
    rotated_rect = rotated_surface.get_rect(center=(ee[0] + hand_offset[0], ee[1] + hand_offset[1]))
    return rotated_surface, rotated_rect.topleft
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    uaqyt = time.localtime()
    minute = - (uaqyt.tm_min * 6)
    second = - (uaqyt.tm_sec * 6)
    screen.fill((255, 255, 255))
    screen.blit(sagat, (0, 0))
    ee = (rct.width // 2, rct.height // 2)
    onkoloff = (10, 0)
    solkoloff = (-10, 0) 
    right_hand, right_pos = rotate_hand(on_kol, minute, ee, onkoloff)
    left_hand, left_pos = rotate_hand(sol_kol, second, ee, solkoloff)
    screen.blit(right_hand, right_pos)
    screen.blit(left_hand, left_pos)
    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()
