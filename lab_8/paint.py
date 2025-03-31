import pygame
import sys




pygame.init()
en, uzyndyq = 800, 600
screen = pygame.display.set_mode((en, uzyndyq))
pygame.display.set_caption("suret salu")
#screen parameters



aq = (255, 255, 255)
qara = (0, 0, 0)
qyzyl = (255, 0, 0)
jasyl = (0, 255, 0)
kok = (0, 0, 255)
tuster = [qara, qyzyl, jasyl, kok]
current_color = qara
salu = False
qyral = "pencil"
font = pygame.font.SysFont(None, 30)
#here color, selections, font



def draw_color_buttons():
    x, y = 10, 10
    button_size = 50
    for index, color in enumerate(tuster):
        pygame.draw.rect(screen, color, pygame.Rect(x, y, button_size, button_size))
        x += button_size + 10
def draw_qyral_buttons():
    pygame.draw.rect(screen, aq, pygame.Rect(10, uzyndyq - 60, 100, 50))
    pygame.draw.rect(screen, qara, pygame.Rect(10, uzyndyq - 60, 100, 50), 5)
    text = font.render("Pencil", True, qara)
    screen.blit(text, (15, uzyndyq - 50))
    pygame.draw.rect(screen, aq, pygame.Rect(120, uzyndyq - 60, 100, 50))
    pygame.draw.rect(screen, qara, pygame.Rect(120, uzyndyq - 60, 100, 50), 5)
    text = font.render("Rectangle", True, qara)
    screen.blit(text, (125, uzyndyq - 50))
    pygame.draw.rect(screen, aq, pygame.Rect(230, uzyndyq - 60, 100, 50))
    pygame.draw.rect(screen, qara, pygame.Rect(230, uzyndyq - 60, 100, 50), 5)
    text = font.render("Circle", True, qara)
    screen.blit(text, (235, uzyndyq - 50))
    pygame.draw.rect(screen, aq, pygame.Rect(340, uzyndyq - 60, 100, 50))
    pygame.draw.rect(screen, qara, pygame.Rect(340, uzyndyq - 60, 100, 50), 5)
    text = font.render("Eraser", True, qara)
    screen.blit(text, (345, uzyndyq - 50))
def draw_shapes():
    if qyral == "rectangle" and salu:
        pygame.draw.rect(screen, current_color, pygame.Rect(basy_x, basy_y, myshka_x - basy_x, myshka_y - basy_y), 2)
    elif qyral == "circle" and salu:
        radius = int(((myshka_x - basy_x)**2 + (myshka_y - basy_y)**2)**0.5)
        pygame.draw.circle(screen, current_color, (basy_x, basy_y), radius, 2)
    elif qyral == "pencil" and salu:
        pygame.draw.line(screen, current_color, (sony_x, sony_y), (myshka_x, myshka_y), 2)
def erase():
    if qyral == "eraser" and salu:
        pygame.draw.rect(screen, aq, pygame.Rect(myshka_x, myshka_y, 10, 10))
#drawing all elements of paint like ( buttons, color of buttons )



screen.fill(aq)
salu = False
basy_x, basy_y = 0, 0
sony_x, sony_y = 0, 0
myshka_x, myshka_y = 0, 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                salu = True
                basy_x, basy_y = event.pos
                sony_x, sony_y = event.pos
            elif event.button == 3:
                salu = False
        elif event.type == pygame.MOUSEMOTION:
            myshka_x, myshka_y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                salu = False
#main game loop



        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 10 <= event.pos[0] <= 60 and 10 <= event.pos[1] <= 60:
                current_color = qara
            elif 70 <= event.pos[0] <= 120 and 10 <= event.pos[1] <= 60:
                current_color = qyzyl
            elif 130 <= event.pos[0] <= 180 and 10 <= event.pos[1] <= 60:
                current_color = jasyl
            elif 190 <= event.pos[0] <= 240 and 10 <= event.pos[1] <= 60:
                current_color = kok
            if 10 <= event.pos[0] <= 110 and uzyndyq - 60 <= event.pos[1] <= uzyndyq - 10:
                qyral = "pencil"
            elif 120 <= event.pos[0] <= 220 and uzyndyq - 60 <= event.pos[1] <= uzyndyq - 10:
                qyral = "rectangle"
            elif 230 <= event.pos[0] <= 330 and uzyndyq - 60 <= event.pos[1] <= uzyndyq - 10:
                qyral = "circle"
            elif 340 <= event.pos[0] <= 440 and uzyndyq - 60 <= event.pos[1] <= uzyndyq - 10:
                qyral = "eraser"
        #color and tool selections of mouse,buttons


    draw_color_buttons()
    draw_qyral_buttons()
    draw_shapes()
    erase()
    #draw color buttons, tool buttons, shapes


    sony_x, sony_y = myshka_x, myshka_y
    #updating last drawn point


    pygame.display.update()
