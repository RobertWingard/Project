import pygame
from pygame.locals import *
import random
from character import Character

pygame.init()
screen_width = 1200
screen_height = 800

#death_count
death_count = 0

# create the display surface object  
# of specific dimension..e(width,height).  
screen = pygame.display.set_mode((screen_width, screen_height))

# set the pygame window name 
pygame.display.set_caption("NeverEndingLOL")

#background image
bg_image = pygame.image.load('background.jpg')



#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0,0))

# object current co-ordinates 
x = screen_width/2
y = screen_height/2

# dimensions of the object 
width = 20
height = 20

# velocity / speed of movement
vel = 10

#hero
goku_start_pos = x,y
goku = Character('goku.xcf',goku_start_pos)



#enemy
mob_start_pos =  100,200#this will be random at some point 
mob = Character('mob.xcf', mob_start_pos)

# Indicates pygame is running
run = True

# infinite loop 
while run:

    #draw background
    draw_bg()


    

    # creates time delay of 10ms 
    pygame.time.delay(10)

    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        goku.move_left(vel)

    if keys[pygame.K_RIGHT] and x<screen_width-(width+goku.get_width()):
        goku.move_right(vel)

    if keys[pygame.K_UP] and y>0:
        goku.move_up(vel)

    if keys[pygame.K_DOWN] and y<screen_height-(height+goku.get_height()):
        goku.move_down(vel)



    screen.blit(goku, (x,y))
    screen.blit(mob, (300,500))

    goku_loc = goku.get_rect(topleft=(x,y))
    mob_loc = mob.get_rect(topleft=(300,500))


    # print(goku_loc)
    # print(mob_loc)
    if goku_loc.colliderect(mob_loc): 
        print('game over')
        break

    # it refreshes the window
    pygame.display.update() 
# closes the pygame window 
pygame.quit()
