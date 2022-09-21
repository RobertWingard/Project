import pygame
from pygame.locals import *
import random







#possibly add in dragonballs and go around and collect them to win the game
#




# import pygame module in this program 
# def bouncing_rect():
#         #draw rect
#     global x_speed, y_speed, other_speed
#     moving_rect.x += x_speed
#     moving_rect.y += y_speed
    #collision with screen borders
    # if moving_rect.right >= screen_width or moving_rect.left <= 0:
    #     x_speed *= -1
    # if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
    #     y_speed *= -1



# collision with screen borders
    # if moving_rect.right >= screen_width and x_speed > 0:
    #     x_speed *= -1
    # if moving_rect.left <= 0 and x_speed < 0:
    #     x_speed *= -1
    # if moving_rect.top <= 0 and y_speed < 0:
    #     y_speed *= -1
    # if moving_rect.bottom >= screen_height and y_speed > 0:
    #     y_speed *= -1



        #moving other rect
    # other_rect.y += other_speed
    # if other_rect.top <= 0 or other_rect.bottom >= screen_height:
    #     other_speed *= -1

        #collision with rect
    # collision_tolerance = 10
    # if moving_rect.colliderect(other_rect):
    #     if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
    #         y_speed *= -1
    #     if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
    #         y_speed *= -1
    #     if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_speed < 0:
    #         x_speed *= -1
    #     if abs(other_rect.left - moving_rect.right) < collision_tolerance and x_speed > 0:
    #         x_speed *= -1


    
    # pygame.draw.rect(screen, (255,255,255),moving_rect)
    # pygame.draw.rect(screen, (255,0,0),other_rect)

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
goku = pygame.image.load("goku.png")
goku_loc = goku.get_rect()
goku = pygame.draw.rect(goku,(255,0,0),[0,0, width, height], 2 )
print(goku_loc)
goku_loc.center = x,y


#enemy
mob = pygame.image.load("mob.png")
mob_loc = mob.get_rect()
print(mob_loc) 
mob_loc.center = 100,200

#test rect
# moving_rect = pygame.Rect(350,350,100,100)
# x_speed, y_speed = 5,4

# #other test rect

# other_rect = pygame.Rect(300,600,200,100)

# other_speed = 2

# Indicates pygame is running
run = True


# infinite loop 
while run:

    #draw background
    draw_bg()

    #damage
    # (currentMobX, currentMobY) = mob_loc.center
    # currentMobXLower = currentMobX - 15, currentMobY
    # currentMobXUpper = currentMobX + 15, currentMobY
    # mob bottom left < goku x is < 
    



    if goku_loc == mob_loc.center:
        print('game over')
        break

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
    if keys[pygame.K_RIGHT] and x<screen_width-(width+goku.get_width()):
        # increment in x co-ordinate
        x += vel
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
        # decrement in y co-ordinate
        y -= vel
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<screen_height-(height+goku.get_height()):
        # increment in y co-ordinate
        y += vel
    # completely fill the surface object  
    # with black colour  
    # win.fill((0, 0, 0))
    # drawing object on screen which is  a rectangle here 
    # pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    goku_loc = (x,y)
    screen.blit(goku, goku_loc)
    screen.blit(mob, (100,200))


    # bouncing_rect()

    # if goku_loc.colliderect(mob):
    #     pygame.draw.rect(screen, (255,0,0), goku_loc, 4)
    # it refreshes the window
    pygame.display.update() 
# closes the pygame window 
pygame.quit()
