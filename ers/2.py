import pygame
import random
 
pygame.init()
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 100)
 
WIDTH = 600
HEIGHT = 400
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
block = 10
speed = 2

 
font = pygame.font.SysFont("Times New Roman", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
  
def score(score):
    value = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])

def snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], block, block])
 
def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])
 
game_over = False
finished = False
x1 = WIDTH / 2
y1 = HEIGHT / 2
dx = 0
dy = 0
snake_List = []
length = 1
fps = 15
 
foodx = round(random.randrange(0, WIDTH - block) / 10.0) * 10.0
foody = round(random.randrange(0, HEIGHT - block) / 10.0) * 10.0
 
while not game_over:
    clock.tick(fps)
                  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and dx != block:
                dx = -block
                dy = 0
            elif event.key == pygame.K_d and dx != -block:
                dx = block
                dy = 0
            elif event.key == pygame.K_w and dy != block:
                    dy = -block
                    dx = 0
            elif event.key == pygame.K_s and dy != - block:
                dy = block
                dx = 0
 
    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
        pygame.quit()
    x1 += dx
    y1 += dy
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [foodx, foody, block, block])
    head = []
    head.append(x1)
    head.append(y1)
    snake_List.append(head)
    if len(snake_List) > length:
        del snake_List[0]
 
    for x in snake_List[:-1]:
        if x == head:
            pygame.quit()
    snake(block, snake_List)
    score(length - 1)

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, WIDTH - block) / 10.0) * 10.0
        foody = round(random.randrange(0, HEIGHT - block) / 10.0) * 10.0
        length += 1
 
        
    pygame.display.update()
pygame.quit()
quit()