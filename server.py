import pygame
from pygame.locals import *
import random

# import pygame module in this program 


pygame.init()
screen_width = 1200
screen_height = 800

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
vel = 5

#hero
goku = pygame.image.load("goku.png")
goku_loc = goku.get_rect() 
goku_loc.center = x,y

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
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
        # decrement in x co-ordinate
        x -= vel
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x<screen_width-width:
        # increment in x co-ordinate
        x += vel
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
        # decrement in y co-ordinate
        y -= vel
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<screen_height-height:
        # increment in y co-ordinate
        y += vel
    # completely fill the surface object  
    # with black colour  
    # win.fill((0, 0, 0))
    # drawing object on screen which is  a rectangle here 
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    # it refreshes the window
    pygame.display.update() 
# closes the pygame window 
pygame.quit()
