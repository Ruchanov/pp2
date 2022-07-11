from sre_parse import WHITESPACE
import pygame as pg
pg.init()

WIDTH,HEIGHT = 800, 600
is_running = True
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('my game')
clock = pg.time.Clock()

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running =False   
    screen.fill((220, 20, 60))
    pg.draw.rect(screen, (0, 255, 0), (WIDTH//2 - 50,HEIGHT//2 - 50,100,100),10)

    for i in range(0,100,10):
        pg.draw.line(screen,(135, 206, 250),(0,15+i),(100,15+i),2)
    pg.display.flip()

pg.quit()