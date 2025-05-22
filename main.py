import pygame #pygame for game development
from pygame.locals import *
import sys
import shop

pygame.init() #init pygame
fps=60 #fps
fpsClock=pygame.time.Clock() #init fps clock
size=(900,700) #windows size
font_counter=pygame.font.SysFont('Arial Black',32)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

button_rect=pygame.Rect(400,200,100,100)
counter=0 #The Global Counter

with open("data/dat","r",encoding="utf-8") as file:
    counter=int(file.read())

counter_text=font_counter.render(str(counter),True,(255,255,255))

#images
earth=pygame.image.load("resources/earth.png").convert_alpha()

print(shop.shop_list[0]["name"])

done=False;
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                counter+=1
                counter_text=font_counter.render(str(counter),True,(255,255,255))
                print(counter)

    #screen
    screen.fill((0,0,0))
    screen.blit(earth,(400,200))
    screen.blit(counter_text,(300,300))
    pygame.display.update()


# git config --global user.name "name"
# git config --global user.email your@email.mail

# Every time you wanna download the newest project file do this:

# git fetch origin
# git merge origin/master

# update

with open("data/dat","w",encoding="utf-8") as file:
    file.write(str(counter))