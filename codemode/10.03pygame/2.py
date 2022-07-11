import pygame as pg
import random

pg.init()
pg.display.set_caption("ellips")
WIDTH = 800
HEIGHT = 600
FPS = 10
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

rect_x = 15
rect_y = 15
dx,dy = 3,3
x=300
y=150
speed = 1
color = RED
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                dx = 1*speed
                dy = 0
            if event.key == pg.K_LEFT:
                dx = -1*speed
                dy = 0
            if event.key == pg.K_DOWN:
                dy = 1 *speed
                dx = 0
            if event.key == pg.K_UP:
                dy = -1*speed
                dx = 0
            if event.key == pg.K_SPACE:
                speed+=1
                dy *= speed
                dx *= speed
            if event.key == pg.KEYDOWN:
                speed+=1
                dy /= speed
                dx /= speed
            

    pg.draw.ellipse(screen,color,(x%WIDTH,y%HEIGHT, 50, 50))
    x+= dx
    y+=dy
    pg.display.flip()
pg.quit()
