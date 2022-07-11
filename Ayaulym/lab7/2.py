import pygame
pygame.init()


_songs = ['ЦыганеизПарижа.mp3', 'Way2Sexy.mp3', 'LostBoy.mp3']
pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((800, 450))
done = False
songpause = False
ord_music = 0
image = pygame.image.load('cover.jpg')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                songpause = not songpause
                if songpause: pygame.mixer.music.pause()
                else: pygame.mixer.music.unpause()
            if event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()
            if event.key == pygame.K_RIGHT:
                if ord_music == len(_songs) - 1:
                    ord_music = 0
                    pygame.mixer.music.load(_songs[ord_music])
                    pygame.mixer.music.play(-1)
                else:
                    ord_music += 1
                    pygame.mixer.music.load(_songs[ord_music])
                    pygame.mixer.music.play(-1)
            if event.key == pygame.K_LEFT:
                if ord_music == 0:
                    ord_music = len(_songs)
                    pygame.mixer.music.load(_songs[ord_music - 1])
                    pygame.mixer.music.play(-1)
                else:
                    ord_music -= 1
                    pygame.mixer.music.load(_songs[ord_music])
                    pygame.mixer.music.play(-1)
        
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pygame.display.flip()