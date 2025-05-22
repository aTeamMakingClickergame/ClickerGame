import pygame #pygame for game development
from pygame.locals import *
import sys
import shop

pygame.init() #init pygame
pygame.display.set_caption("A Click Game")
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

characters=[
    pygame.image.load("resources/ShopVolunteer.png").convert_alpha(),
    pygame.image.load("resources/ShopGardener.png").convert_alpha(),
    pygame.image.load("resources/ShopForester.png").convert_alpha(),
    pygame.image.load("resources/ShopDryad.png").convert_alpha(),
    pygame.image.load("resources/ShopSpecialist.png").convert_alpha(),
    pygame.image.load("resources/ShopGodOfNature.png").convert_alpha()
]
characters_description=[]

# print(characters[0])

print(shop.shop_list[0]["name"])

done=False;
while not done:
    Pos=pygame.mouse.get_pos
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
    #
    screen.blit(characters[0],(20,25))
    screen.blit(characters[1],(20,130))
    screen.blit(characters[2],(20,235))
    screen.blit(characters[3],(20,340))
    screen.blit(characters[4],(20,445))
    screen.blit(characters[5],(20,550))
    #
    characters_description=[
        font_counter.render(str("Volunteer"),True,(255,255,255)),
        font_counter.render(str("Gardner"),True,(255,255,255)),
        font_counter.render(str("Forester"),True,(255,255,255)),
        font_counter.render(str("Dryad"),True,(255,255,255)),
        font_counter.render(str("Specialist"),True,(255,255,255)),
        font_counter.render(str("God Of Nature"),True,(255,255,255))
    ]
    screen.blit(characters_description[0],(70,25))
    screen.blit(characters_description[1],(70,130))
    screen.blit(characters_description[2],(70,235))
    screen.blit(characters_description[3],(70,340))
    screen.blit(characters_description[4],(70,445))
    screen.blit(characters_description[5],(70,550))
    pygame.display.update()


# git config --global user.name "name"
# git config --global user.email your@email.mail

# Every time you wanna download the newest project file do this:

# git fetch origin
# git merge origin/master

# update

with open("data/dat","w",encoding="utf-8") as file:
    file.write(str(counter))