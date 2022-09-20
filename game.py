import pygame
from pygame.locals import *
import random

size = screen_width, screen_height = (1400,800)
speed = 1


pygame.init()
running = True
screen = pygame.display.set_mode((size))
pygame.display.set_caption("NeverEndingLOL")
bg_image = pygame.image.load('background.jpg').convert_alpha()


#drawing new method
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (size))
    screen.blit(scaled_bg, (0,0))




clock = pygame.time.Clock()
FPS = 60


clock.tick(FPS)

# pygame.display.update()

# velocity / speed of movement
vel = 5

# object current co-ordinates 
x = screen_width/2
y = screen_height/2

#hero
goku = pygame.image.load("goku.png")
goku_loc = goku.get_rect() 
# goku_loc.center = screen_height

#enemy
# mob = pygame.image.load("mob.png")
# mob_loc = mob.get_rect() 
# mob_loc.center = screen_height*0.2

counter = 0 
#game loop

#background image
draw_bg()

while running:
    counter += 1
    if counter == 5000:
        speed += 0.10
        counter = 0
        print(' level up', speed)
    #animate enemy
    # mob_loc[1] += speed
    # if mob_loc[1] > screen_height:
    #     if random.randint(0,1) == 0:
    #         mob_loc.center = right_lane, -200
    #     else:
    #         mob_loc.center = left_lane, -200

#damage
    if mob_loc.center == goku_loc.center:
    #  if goku_loc[0] == mob_loc[0] and mob_loc[1] > goku_loc[1] - 250:
        print('game over')
        break

    #event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
        # decrement in x co-ordinate
        x -= vel
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x<screen_width:
        # increment in x co-ordinate
        x += vel
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
        # decrement in y co-ordinate
        y -= vel
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<screen_height:
        # increment in y co-ordinate
        y += vel
    # completely fill the surface object  
    # with black colour  
    # win.fill((0, 0, 0))
    # drawing object on screen which is  a rectangle here 
    # pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    # it refreshes the window
    # pygame.display.update() 
    screen.blit(goku, (x,y))
    # screen.blit(mob, mob_loc)
    pygame.display.update()

pygame.quit()