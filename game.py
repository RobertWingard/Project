import pygame
from pygame.locals import *
import random

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

# Indicates pygame is running
run = True

# infinite loop 
while run:

    draw_bg()

    # creates time delay of 10ms 
    pygame.time.delay(10)


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