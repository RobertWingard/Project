import pygame
from pygame.locals import *
import random
from character import Character,Enemy
import time


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

#loop to get mob to spawn randomly
# def spawn():
#     mob_count = 0
#     # spawn enemy randomly around the screen
#     if mob_count == 0
#     # mob_start_pos = random 
#         spawn mob =  random.randint(random,random)
    # mob = Character(mob_start_pos, 'mob.xcf')    image
    # move mob left or right across the screen.



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
goku = Character(goku_start_pos, 'goku.xcf')



#enemy
mob_start_pos =  100,200 #this will be random at some point 
mob1 = Enemy(mob_start_pos, 'mob.xcf')
mob2 = Enemy(mob_start_pos, 'mob.xcf')
mob3 = Enemy(mob_start_pos, 'mob.xcf')
mob4 = Enemy(mob_start_pos, 'mob.xcf')
mob5 = Enemy(mob_start_pos, 'mob.xcf')

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
    if keys[pygame.K_LEFT] and goku.currentX>0:
        goku.move_left()

    if keys[pygame.K_RIGHT] and goku.currentX<screen_width-(width+goku.image.get_width()):
        goku.move_right()

    if keys[pygame.K_UP] and goku.currentY>0:
        goku.move_up()

    if keys[pygame.K_DOWN] and goku.currentY<screen_height-(height+goku.image.get_height()):
        goku.move_down()



    goku.draw(screen)
    mob1.draw(screen)
    mob2.draw(screen)
    mob3.draw(screen)
    mob4.draw(screen)
    # mob5.draw(screen)

    goku_loc = goku.rect
    mob_loc1 = mob1.rect
    mob_loc2 = mob2.rect
    mob_loc3 = mob3.rect
    mob_loc4 = mob4.rect
    # mob_loc5 = mob5.rect

    if goku_loc.colliderect(mob_loc1) or goku_loc.colliderect(mob_loc2) or goku_loc.colliderect(mob_loc3) or goku_loc.colliderect(mob_loc4): #or goku_loc.colliderect(mob_loc5) : 
        print('game over')
        time.sleep(5)
        mob1.x = random.choice([0,1200])
        mob2.x = random.choice([0,1200])
        mob3.x = random.choice([0,1200])
        mob4.x = random.choice([0,1200])
        continue

    # it refreshes the window
    pygame.display.update() 
# closes the pygame window 
pygame.quit()
