from turtle import down
import pygame as pg
import random

pg.init()

pg.mixer.init()
pg.mixer.music.load("./music/background.mp3")
pg.mixer.music.play(-1)

WIDTH = 800
HEIGHT = 600
FPS = 50

#background_img = pg.image.load("./images/background.jpg")
#background_img = pg.transform.scale(background_img, (WIDTH, HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE=(0,0,225)
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
font = pg.font.SysFont("Georgia", 18)
x = 0
y = 0
color = RED
el_x,el_y = WIDTH//2,HEIGHT//2
dx, dy = 2, 4
running = True
while running:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and x>=35:
                x -= 35
            if event.key == pg.K_s and x+80-35<=WIDTH:
                x += 35
            if event.key == pg.K_UP and y>=35:
                y -= 35
            if event.key == pg.K_DOWN and y+80-35<=WIDTH:
                y += 35
        
    screen.fill(BLACK)
    pg.draw.line(screen, WHITE,(395, 0),(395, 600), 10)
    pg.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 100, 5)
    pg.draw.line(screen, RED,(10,x),(10,x+100),10)
    pg.draw.line(screen, BLUE,(WIDTH-10,y),(WIDTH-10,y+100),10)
    pg.draw.line(screen, RED,(10,x),(10,x+80),10)
    pg.draw.line(screen, BLUE,(WIDTH-10,y),(WIDTH-10,y+80),10)
    pg.draw.ellipse(screen,color,(el_x,el_y, 20, 20))
    if el_y<=0 or  el_y>=HEIGHT-20:
        dy *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if el_x<=10 and el_y>=x and el_y<=x+80:
        dx*=-1
    if el_x>=WIDTH-30 and el_y>=y and el_y<=y+80:
        dx*=-1
    if el_x<10:
        pg.draw.rect(screen, WHITE, (WIDTH // 2 - 200,
                     HEIGHT // 2 - 200, 300, 50))
        text1 = font.render('RIGHT PLAYER WIN', False, False)
        screen.blit(text1, (WIDTH // 2 - 200, HEIGHT // 2 - 200))
        #screen.blit(text2, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
    if el_x>WIDTH:
        pg.draw.rect(screen, WHITE, (WIDTH // 2 - 200,
                     HEIGHT // 2 - 200, 300, 50))
        text1 = font.render('LEFT PLAYER WIN', False, False)
        screen.blit(text1, (WIDTH // 2 - 200, HEIGHT // 2 - 200))
    el_x += dx
    el_y += dy

    pg.display.flip()
pg.quit()
