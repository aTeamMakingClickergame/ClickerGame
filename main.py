import pygame #pygame for game development
from pygame.locals import *
import sys
import shop
pygame.init() #init pygame
pygame.display.set_caption("A Click Game")
fps=60 #fps
fpsClock=pygame.time.Clock() #init fppis clock
size=(900,700) #windows size
font_counter=pygame.font.SysFont('Arial Black',32)
statsfont=pygame.font.SysFont('Arial Black',20)

screen=pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

button_rect=pygame.Rect(400,200,100,100)
counter=0 #The Global Counter

with open("data/dat","r",encoding="utf-8") as file:
    counter=int(file.read())

counter_text=font_counter.render(str(counter),True,(255,255,255))

def reform(num):
    if(num>=1000000000000):
        return str(round(float(num)/1000000000000,2))+"T"
    if(num>=1000000000):
        return str(round(float(num)/1000000000,2))+"B"
    if(num>=1000000):
        return str(round(float(num)/1000000,2))+"M"
    if(num>=1000):
        return str(round(float(num)/1000,2))+"K"
    return str(num)

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
trees=[
    pygame.image.load("resources/TreeOak.png").convert_alpha(),
    pygame.image.load("resources/TreeBirch.png").convert_alpha(),
    pygame.image.load("resources/TreeCherry.png").convert_alpha(),
    pygame.image.load("resources/TreeMaple.png").convert_alpha(),
    pygame.image.load("resources/TreeGolden.png").convert_alpha(),
    pygame.image.load("resources/TreeBinary.png").convert_alpha()
]

character_price=[
    50,250,10000,1000000,50000000,1000000000
]
tree_price=[
    100,30000,500000,1000000000,25000000000,100000000000
]

Volunteer=0;
Gardener=0;
Forester=0;
Dryad=0;
Specialist=0;
God=0;

characters_description=[]

# print(characters[0])

#Trees Here

#Oak 100 +100%
#Birch 30000 +100%
#Cherry 5000000
#Maple 1000000000
#Golden 25000000000
#Binary 100000000000
Oak=0
Birch=0
Cherry=0
Maple=0
Golden=0
Binary=0


print(shop.shop_list[0]["name"])

def UpdCharacters():
    if characters_rect[0].collidepoint(Pos):
        characters_description[0]=font_counter.render(str("Volunteer"),True,(0,255,0))
    elif characters_rect[1].collidepoint(Pos):
        characters_description[1]=font_counter.render(str("Gardner"),True,(0,255,0))
    elif characters_rect[2].collidepoint(Pos):
        characters_description[2]=font_counter.render(str("Forester"),True,(0,255,0))
    elif characters_rect[3].collidepoint(Pos):
        characters_description[3]=font_counter.render(str("Dryad"),True,(0,255,0))
    elif characters_rect[4].collidepoint(Pos):
        characters_description[4]=font_counter.render(str("Specialist"),True,(0,255,0))
    elif characters_rect[5].collidepoint(Pos):
        characters_description[5]=font_counter.render(str("God Of Nature"),True,(0,255,0))

def UpdTrees():
    if trees_rect[0].collidepoint(Pos):
        trees_description[0]=font_counter.render(str("Oak Tree"),True,(0,255,0))
    elif trees_rect[1].collidepoint(Pos):
        trees_description[1]=font_counter.render(str("Birch Tree"),True,(0,255,0))
    elif trees_rect[2].collidepoint(Pos):
        trees_description[2]=font_counter.render(str("Cherry Tree"),True,(0,255,0))
    elif trees_rect[3].collidepoint(Pos):
        trees_description[3]=font_counter.render(str("Maple Tree"),True,(0,255,0))
    elif trees_rect[4].collidepoint(Pos):
        trees_description[4]=font_counter.render(str("Golden Tree"),True,(0,255,0))
    elif trees_rect[5].collidepoint(Pos):
        trees_description[5]=font_counter.render(str("Binary Tree"),True,(0,255,0))


done=False
pygame.time.set_timer(USEREVENT,1000)

while not done:
    TreePerSecond=statsfont.render(reform(1*Volunteer+6*Gardener+50*Forester+1000*Dryad+100000*Specialist+1000000*God)+" Trees Per Second",True,(0,0,255))
    TreePerClick=statsfont.render(reform(1*(1+Oak)*(1+Birch*2)*(1+Cherry*3)*(1+Maple*4)*(1+Golden*5)*(1+Binary*6))+" Trees Per Click",True,(0,0,255))
    
    Pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                counter+=1*(1+Oak)*(1+Birch*2)*(1+Cherry*3)*(1+Maple*4)*(1+Golden*5)*(1+Binary*6)
                print(counter)
            bought=False
            if characters_rect[0].collidepoint(event.pos) and counter>=character_price[0]*int(1.1**Volunteer):
                counter-=(character_price[0]*int(1.1**Volunteer))
                bought=True
                Volunteer+=1
                print(Volunteer)
            if characters_rect[1].collidepoint(event.pos) and counter>=character_price[1]*int(1.1**Gardener):
                counter-=(character_price[1]*int(1.1**Gardener))
                bought=True
                Gardener+=1
                print(Gardener)
            if characters_rect[2].collidepoint(event.pos) and counter>=character_price[2]*int(1.1**Forester):
                counter-=(character_price[2]*int(1.1**Forester))
                bought=True
                Forester+=1
                print(Forester)
            if characters_rect[3].collidepoint(event.pos) and counter>=character_price[3]*int(1.1**Dryad):
                counter-=(character_price[3]*int(1.1**Dryad))
                bought=True
                Dryad+=1
                print(Dryad)
            if characters_rect[4].collidepoint(event.pos) and counter>=character_price[4]*int(1.1**Specialist):
                counter-=(character_price[4]*int(1.1**Specialist))
                bought=True
                Specialist+=1
                print(Specialist)
            if characters_rect[5].collidepoint(event.pos) and counter>=character_price[5]*int(1.1**God):
                counter-=(character_price[5]*int(1.1**God))
                bought=True
                God+=1
                print(God)
            if trees_rect[0].collidepoint(event.pos) and counter>=tree_price[0]*int(1.1**Oak):
                counter-=(tree_price[0]*int(1.1**Oak))
                bought=True
                Oak+=1
                print(Oak)
            if trees_rect[1].collidepoint(event.pos) and counter>=tree_price[1]*int(1.1**Birch):
                counter-=(tree_price[1]*int(1.1**Birch))
                bought=True
                Birch+=1
                print(Birch)
            if trees_rect[2].collidepoint(event.pos) and counter>=tree_price[2]*int(1.1**Cherry):
                counter-=(tree_price[2]*int(1.1**Cherry))
                bought=True
                Cherry+=1
                print(Cherry)
            if trees_rect[3].collidepoint(event.pos) and counter>=tree_price[3]*int(1.1**Maple):
                counter-=(tree_price[3]*int(1.1**Maple))
                bought=True
                Maple+=1
                print(Maple)
            if trees_rect[4].collidepoint(event.pos) and counter>=tree_price[4]*int(1.1**Golden):
                counter-=(tree_price[4]*int(1.1**Golden))
                bought=True
                Golden+=1
                print(Golden)
            if trees_rect[5].collidepoint(event.pos) and counter>=tree_price[5]*int(1.1**Binary):
                counter-=(tree_price[5]*int(1.1**Binary))
                bought=True
                Binary+=1
                print(Binary)
            if bought:
                pygame.display.update()
                break
        if event.type==USEREVENT:
            counter+=(1*Volunteer+6*Gardener+50*Forester+1000*Dryad+100000*Specialist+1000000*God)
            pygame.display.update()
            
    counter_text=font_counter.render(reform(counter),True,(0,127,0))
    #screen
    screen.fill((0,0,0))
    screen.blit(earth,(400,200))
    screen.blit(counter_text,(450-counter_text.get_width()/2,350))
    screen.blit(TreePerSecond,(450-TreePerSecond.get_width()/2,400))
    screen.blit(TreePerClick,(450-TreePerClick.get_width()/2,450))
    #
    #rects
    characters_rect=[
        pygame.Rect(20,25,300,85),
        pygame.Rect(20,130,300,85),
        pygame.Rect(20,235,300,85),
        pygame.Rect(20,340,300,85),
        pygame.Rect(20,445,300,85),
        pygame.Rect(20,550,300,85)
    ]
    trees_rect=[
        pygame.Rect(580,25,300,85),
        pygame.Rect(580,130,300,85),
        pygame.Rect(580,235,300,85),
        pygame.Rect(580,340,300,85),
        pygame.Rect(580,445,300,85),
        pygame.Rect(580,550,300,85)
    ]
    
    screen.blit(characters[0],(20,25))
    screen.blit(characters[1],(20,130))
    screen.blit(characters[2],(20,235))
    screen.blit(characters[3],(20,340))
    screen.blit(characters[4],(20,445))
    screen.blit(characters[5],(20,550))
    
    screen.blit(trees[0],(835,25))
    screen.blit(trees[1],(835,130))
    screen.blit(trees[2],(835,235))
    screen.blit(trees[3],(835,340))
    screen.blit(trees[4],(835,445))
    screen.blit(trees[5],(835,550))
    #
    characters_description=[
        font_counter.render(str("Volunteer"),True,(255,255,255)),
        font_counter.render(str("Gardner"),True,(255,255,255)),
        font_counter.render(str("Forester"),True,(255,255,255)),
        font_counter.render(str("Dryad"),True,(255,255,255)),
        font_counter.render(str("Specialist"),True,(255,255,255)),
        font_counter.render(str("God Of Nature"),True,(255,255,255))
    ]
    trees_description=[
        font_counter.render(str("Oak Tree"),True,(255,255,255)),
        font_counter.render(str("Birch Tree"),True,(255,255,255)),
        font_counter.render(str("Cherry Tree"),True,(255,255,255)),
        font_counter.render(str("Maple Tree"),True,(255,255,255)),
        font_counter.render(str("Golden Tree"),True,(255,255,255)),
        font_counter.render(str("Binary Tree"),True,(255,255,255))
    ]
    #
    characters_price_tag=[
        font_counter.render(reform(int(character_price[0]*(1.1**Volunteer)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(character_price[1]*(1.1**Gardener)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(character_price[2]*(1.1**Forester)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(character_price[3]*(1.1**Dryad)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(character_price[4]*(1.1**Specialist)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(character_price[5]*(1.1**God)))+" Trees",True,(255,255,255))
    ]
    trees_price_tag=[
        font_counter.render(reform(int(tree_price[0]*(1.1**Oak)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(tree_price[1]*(1.1**Birch)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(tree_price[2]*(1.1**Cherry)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(tree_price[3]*(1.1**Maple)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(tree_price[4]*(1.1**Golden)))+" Trees",True,(255,255,255)),
        font_counter.render(reform(int(tree_price[5]*(1.1**Binary)))+" Trees",True,(255,255,255))
    ]
    UpdCharacters()
    UpdTrees()
    # pic: 85x45
    screen.blit(characters_description[0],(70,25))
    screen.blit(characters_description[1],(70,130))
    screen.blit(characters_description[2],(70,235))
    screen.blit(characters_description[3],(70,340))
    screen.blit(characters_description[4],(70,445))
    screen.blit(characters_description[5],(70,550))
    
    screen.blit(trees_description[0],(830-trees_description[0].get_width(),25))
    screen.blit(trees_description[1],(830-trees_description[1].get_width(),130))
    screen.blit(trees_description[2],(830-trees_description[2].get_width(),235))
    screen.blit(trees_description[3],(830-trees_description[3].get_width(),340))
    screen.blit(trees_description[4],(830-trees_description[4].get_width(),445))
    screen.blit(trees_description[5],(830-trees_description[5].get_width(),550))
    #
    screen.blit(characters_price_tag[0],(70,55))
    screen.blit(characters_price_tag[1],(70,160))
    screen.blit(characters_price_tag[2],(70,265))
    screen.blit(characters_price_tag[3],(70,370))
    screen.blit(characters_price_tag[4],(70,475))
    screen.blit(characters_price_tag[5],(70,580))
    
    screen.blit(trees_price_tag[0],(830-trees_price_tag[0].get_width(),55))
    screen.blit(trees_price_tag[1],(830-trees_price_tag[1].get_width(),160))
    screen.blit(trees_price_tag[2],(830-trees_price_tag[2].get_width(),265))
    screen.blit(trees_price_tag[3],(830-trees_price_tag[3].get_width(),370))
    screen.blit(trees_price_tag[4],(830-trees_price_tag[4].get_width(),475))
    screen.blit(trees_price_tag[5],(830-trees_price_tag[5].get_width(),580))
    pygame.display.update()


# git config --global user.name "name"
# git config --global user.email your@email.mail

# Every time you wanna download the newest project file do this:

# git fetch origin
# git merge origin/master

# update

with open("data/dat","w",encoding="utf-8") as file:
    file.write(str(counter))