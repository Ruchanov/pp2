import pygame as pg
import random

pg.init()
pg.display.set_caption("ellips")
WIDTH = 800
HEIGHT = 600
FPS = 100
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
                x += 5
                #dy = 0
            if event.key == pg.K_LEFT:
                x -= 5
                #dy = 0
            if event.key == pg.K_DOWN:
                y += 5
                #dx = 0
            if event.key == pg.K_UP:
                y -= 5
                #dx = 0
            

    pg.draw.ellipse(screen,color,(x%WIDTH,y%HEIGHT, 50, 50))
    #x+= dx
    #y+=dy
    pg.display.flip()
pg.quit()