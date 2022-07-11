import pygame as pg
from datetime import datetime
pg.init()

WIDTH, HEIGHT = 800, 600
FPS = 45

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('clock')

clock = pg.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def blitRotate(surf,image,topleft,angle):
    rotated_image = pg.transform.rotate(image,angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image,new_rect)
    
background = pg.image.load("background.jpg")
h = pg.image.load("min.png")
h2 = pg.image.load("sec.png")

def time(time):
    return 360-time*6

font = pg.font.SysFont("Times New Roman",40)

running = True
while running:
    clock.tick(1)
    #keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(background,(0,0))
    t=datetime.now()
    angle_sec = time(t.second)
    angle_min = time(t.minute)

    blitRotate(screen,h,(255,150),angle_min)
    blitRotate(screen,h2,(255,150),angle_sec)

   
    pg.display.flip()
pg.quit()