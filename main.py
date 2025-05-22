import pygame #pygame for game development
from pygame.locals import *
import sys

pygame.init() #init pygame
fps=60 #fps
fpsClock=pygame.time.Clock() #init fps clock
size=(700,500) #windows size
font_counter=pygame.font.SysFont('Arial',32)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

button_rect=pygame.Rect(300,150,100,100)
button_color=(0,128,0)
text_color=(0,0,0)
counter=0 #The Global Counter
counter_text=font_counter.render(str(counter),True,(255,255,255))

done = False;
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                counter+=1
                counter_text=font_counter.render(str(counter),True,(255,255,255))
                print(counter)
    screen.fill((0,139,139))
    pygame.draw.rect(screen,button_color,button_rect)
    screen.blit(counter_text,(300,300))
    pygame.display.update()


# git config --global user.name "name"
# git config --global user.email your@email.mail

# Every time you wanna download the newest project file do this:

# git fetch origin
# git merge origin/master

# update