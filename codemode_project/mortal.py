import pygame
from random import randint, randrange
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREENYELLOW = (173, 255, 47)
BLUE = (0, 0, 255)
PURPLE = (221, 160, 221)
GRAY = (128, 128, 128)

font_small = pygame.font.SysFont("Verdana", 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mortal Nursat')

finished = False


class Column(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(20,HEIGHT)
        self.image = pygame.image.load("./images/column.png")
        self.dlina = randint(0, HEIGHT)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH + 50, 0)

    def move(self):
        self.rect.move_ip = (-5, 0)

    def draw(self):
        self.surf.blit(pygame.transform.scale(
            self.image, (20, HEIGHT)), (WIDTH+50, 0))
        screen.blit(self.surf, (self.rect))


columns = pygame.sprite.Group()
columns.add(Column)

clock = pygame.time.Clock()

image = pygame.image.load("./images/mortal.jpg")

while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
    columns.draw()
    columns.move()

    screen.blit(pygame.transform.scale(image, (WIDTH, HEIGHT)), (0, 0))

    pygame.display.flip()
pygame.quit()
