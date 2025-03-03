# Reprodutor de áudio MP3
import pygame
import time

pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('oi.mp3')
pygame.mixer_music.play(0, 0)

pygame.mixer.music.set_endevent()
end_of_song = pygame.mixer.music.get_endevent()
time.sleep(5)
print(end_of_song)
time.sleep(10)



