import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
print('MORTAL KOMBAT!')
pygame.mixer.music.play()
input()
pygame.event.wait()
