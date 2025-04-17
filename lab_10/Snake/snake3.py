import pygame
import random
import sys
import os
import psycopg2




def connect_db():
    try:
        return psycopg2.connect(
            dbname="postgres",  
            user="postgres",    
            password="12345",   
            host="localhost",   
            port="5432"         
        )
    except psycopg2.Error as e:
        print("PostgreSQL серверіне қосылу қатесі:", e)
        sys.exit(1)
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(50) NOT NULL UNIQUE
                      );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_score (
                        user_id INT NOT NULL,
                        score INT DEFAULT 0,
                        level INT DEFAULT 1,
                        PRIMARY KEY (user_id),
                        FOREIGN KEY (user_id) REFERENCES users(id)
                      );''')
    conn.commit()
    cursor.close()
    conn.close()
create_tables()
def get_user_info(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    if user is None:       
        cursor.execute('INSERT INTO users (username) VALUES (%s) RETURNING id', (username,))
        user_id = cursor.fetchone()[0]
        cursor.execute('INSERT INTO user_score (user_id) VALUES (%s)', (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return user_id, 0, 1  
    else:
        user_id = user[0]
        cursor.execute('SELECT score, level FROM user_score WHERE user_id = %s', (user_id,))
        score, level = cursor.fetchone()
        cursor.close()
        conn.close()
        return user_id, score, level
def start_game():
    pygame.init()
    en = 600
    uzyndyq = 400
    olshem = 20
    kok = (0, 150, 255)
    qyzyl = (255, 0, 0)
    aq = (255, 255, 255)
    screen = pygame.display.set_mode((en, uzyndyq))
    pygame.display.set_caption("Snake ойыны")
    arty = pygame.image.load(os.path.join("Snake", "bgjpg.jpg"))
    arty = pygame.transform.scale(arty, (en, uzyndyq))
    clock = pygame.time.Clock()
    jylan_speed = 10
    jylan = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    username = input("Atyndy engiz:  ")
    user_id, score, level = get_user_info(username)
    def generate_food():
        while True:
            x = random.randrange(0, en, olshem)
            y = random.randrange(0, uzyndyq, olshem)
            if (x, y) not in jylan:
                return (x, y)
    alma_orny = generate_food()
    font = pygame.font.SysFont(None, 30)
    def draw_text(text, x, y, color=aq):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))
    running = True
    pause = False  
    while running:
        screen.blit(arty, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  
                    pause = not pause
                    if pause:                       
                        conn = connect_db()
                        cursor = conn.cursor()
                        cursor.execute('UPDATE user_score SET score = %s, level = %s WHERE user_id = %s',
                                       (score, level, user_id))
                        conn.commit()
                        cursor.close()
                        conn.close()
                        print("Oiyn toktady jane saktaldy.")
                elif not pause:
                    if event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"
                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"
        if not pause:
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
            if head_x < 0 or head_x >= en or head_y < 0 or head_y >= uzyndyq or new_head in jylan:
                running = False
            jylan.insert(0, new_head)
            if new_head == alma_orny:
                score += 1
                if score % 3 == 0:
                    level += 1
                    jylan_speed += 2  
                alma_orny = generate_food()
            else:
                jylan.pop()
            pygame.draw.rect(screen, qyzyl, (alma_orny[0], alma_orny[1], olshem, olshem))
            for segment in jylan:
                pygame.draw.rect(screen, kok, (segment[0], segment[1], olshem, olshem))
            draw_text(f"Score: {score}", 10, 10)
            draw_text(f"Level: {level}", 10, 30)
        pygame.display.update()
        clock.tick(jylan_speed)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE user_score SET score = %s, level = %s WHERE user_id = %s',
                   (score, level, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Oiyn toktady jane saktaldy")

    pygame.quit()
    sys.exit()


start_game()
