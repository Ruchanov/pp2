import pygame as pg
import random

pg.init()
pg.display.set_caption("сircle")
WIDTH = 800
HEIGHT = 600
FPS = 100
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
x=WIDTH//2
y=HEIGHT//2
color = RED
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if keys[pg.K_RIGHT] and x+25<WIDTH:
        x += 20
    if keys[pg.K_LEFT] and x>25:
        x -= 20
    if keys[pg.K_DOWN] and y+25<HEIGHT:
        y += 20
    if keys[pg.K_UP] and y>25:
        y -= 20

            
    pg.draw.circle(screen,color,(x,y),25)

    pg.display.flip()
pg.quit()