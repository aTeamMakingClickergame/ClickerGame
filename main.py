import pygame #pygame for game development
import sys

pygame.init() #init pygame
fps=60
fpsClock=pygame.time.Clock()

size=(700,500) #windows size

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

done = False;
while not done:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            done=True
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,0,0),[50,50,50,50])
    pygame.display.update()


# git config --global user.name "name"
# git config --global user.email your@email.mail

# Every time you wanna download the newest project file do this:

# git fetch origin
# git merge origin/master

# update