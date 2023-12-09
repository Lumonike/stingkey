import pygame
from random import randint
import time
sneak = False
bg_color = (0, 200, 0)
are=0
gee=0
be=200
x2=700
y2=700
#Background color
#set screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
delta = time.time()
#set name
pygame.display.set_caption("pygame platrofmer")

#update screen
pygame.display.flip()

#boolean window is running
running = True

# blue square cords
x1, y1, w, h = 30, 30, 50, 50
changex, changey = 0, 0
E = 15
cool=False
cooltime=0
screen_width, screen_height = screen.get_size()
#game loop
#  - input arrow keys
#  - change funny fella moving
#  - output displaying
Not = time.time()
Sneak1 = time.time()
while running:
    x, y = pygame.mouse.get_pos()
    delta = time.time()
    #get input
    for event in pygame.event.get():

        #check if window was closed 
        if event.type == pygame.QUIT:
            running = False

        #check is key
        elif event.type == pygame.KEYDOWN:
            #check if key is right key
            if event.key == pygame.K_r:
                x1 = randint(0, screen_width-w)
                y1 = randint(0, screen_height-h)

            elif event.key == pygame.K_t:
                #print(time.time(), Sneak1, cooltime, cool)
                if cool==False and not sneak:
                    sneak = True
                    #TURN IT INVIS
                    gee=198
                    be=0
                    Sneak1 = time.time()

            elif event.key == pygame.K_ESCAPE:
                #dies
                running = False
            
            elif event.key == pygame.K_RIGHT:
                changex += E
        
            elif event.key == pygame.K_LEFT:
                changex -= E

            elif event.key == pygame.K_UP:
                changey -= E
        
            elif event.key == pygame.K_DOWN:
                changey += E

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                changex+=E
            elif event.key == pygame.K_RIGHT:
                changex-=E
            elif event.key == pygame.K_UP:
                changey+=E
            elif event.key == pygame.K_DOWN:
                changey-=E

    if x2>x1 and not gee==198:
        x2-=7
    elif x2<x1 and not gee==198:
        x2+=7
    if y2>y1 and not gee==198:
        y2-=7
    elif y2<y1 and not gee==198:
        y2+=7




    #changes
    x1 += changex
    y1 += changey
    




    if time.time()-Sneak1>5 and sneak:
        be=200
        gee=0
        cool=True
        sneak = False
        #TURN IUT BAG
        cooltime=time.time()
    if time.time()-cooltime>10 and cool:
        cool = False


    if x1<x<x1+w and y1<y<y1+h:
        running = False
    if x1<=x2<=x1+w and y1<=y2<=y1+h:
        running = False
    if x1<=x2+w<=x1+w and y1<=y2+h<=y1+h:
        running = False
        
    if x1>screen_width:
        if time.time()-Not>2:
            running = False
    elif x1<0:
        if time.time()-Not>2:
            running = False
    elif y1<0:
        if time.time()-Not>2:
            running = False
    elif y1>screen_height:
        if time.time()-Not>2:
            running = False
    else:
        Not = time.time()

    #output
    #set screen background
    screen.fill(bg_color)
    pygame.draw.rect(screen, (are, gee, be), pygame.Rect(x1, y1, w, h))
    pygame.draw.rect(screen, (90, 0, 0), pygame.Rect(x2, y2, w, h))
    pygame.display.flip()