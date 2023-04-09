import pygame as pg
import random

pg.init()
pg.display.set_caption("square moving")
WIDTH = 800
HEIGHT = 600
FPS = 100000
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

rect_x = 10
rect_y = 10
dx,dy = 3,3
x=300
y=150
color = RED
running = True
screen.fill(WHITE)
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    pg.draw.rect(screen,color,(x+dx,y+dy, rect_x, rect_y))
    x+=dx
    y+=dy
    

    if x >= WIDTH - rect_x or x<= 0:
        dx*=-1
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    if y>=HEIGHT - rect_y or y<=0:
        dy*=-1
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    pg.display.flip()
pg.quit()