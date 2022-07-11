import pygame
pygame.init()


_songs = ['ЦыганеизПарижа.mp3', 'Way2Sexy.mp3', 'LostBoy.mp3']
pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((800, 450))
done = False
songpause = False
ord_music = 0
image = pygame.image.load('cover.png')

while not done: