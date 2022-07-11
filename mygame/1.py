from pickle import FALSE
import pygame as pg
import random

pg.init()

pg.mixer.init()
pg.mixer.music.load("./music/background.mp3")
pg.mixer.music.play(-1)

WIDTH = 800
HEIGHT = 600
FPS = 50

background_img = pg.image.load("./images/background.jpg")
background_img = pg.transform.scale(background_img, (WIDTH, HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
font = pg.font.SysFont("Georgia", 18)

dx,dy = 3,3
x=0
y=0
m =500
k =200
dm,dk = 3,3
z=0
score = 0
color = RED
running = True
while running:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                z += 35
            if event.key == pg.K_LEFT:
                z -= 35
    pg.draw.ellipse(screen,color,(x,y, 40, 40))
    pg.draw.line(screen,BLACK,(0+z,550),(100+z,550),20)
    if x >=760 or x < 0:
        dx *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if y < 0:
        dy *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if x>=0+z and x<=100+z and y==510:
        score +=1
        dy *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    '''if score>=1:
        pg.draw.ellipse(screen,color,(m,k, 40, 40))
        if m >=760 or m < 0:
            dm *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if k < 0:
            dk *= -1
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if m>=0+z and m<=100+z and k==480:
            score +=1
            dk *= -1
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        m+=dm
        k+=dk
    '''

    if y>=HEIGHT:
        text2 = f'Game over\n Total score is:{score}'
        r2 = font.render(text2, True, BLACK)
        screen.blit(r2, (WIDTH//2, HEIGHT//2))    
    x+= dx
    y+=dy

    text1 = f'score:{score}'
    r = font.render(text1, True, BLACK)
    screen.blit(r, (10, 0))
    pg.display.flip()
pg.quit()
