import pygame
from pygame.locals import *
import random

size = width, height = (1200,800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode((size))
pygame.display.set_caption("NeverEndingLOL")
screen.fill((60,220,0))



pygame.display.update()




#hero
goku = pygame.image.load("goku.png")
goku_loc = goku.get_rect() 
goku_loc.center = right_lane, height*0.8

#enemy
mob = pygame.image.load("mob.png")
mob_loc = mob.get_rect() 
mob_loc.center = left_lane, height*0.2

counter = 0 
#game loop
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print(' level up', speed)
    #animate enemy
    mob_loc[1] += speed
    if mob_loc[1] > height:
        if random.randint(0,1) == 0:
            mob_loc.center = right_lane, -200
        else:
            mob_loc.center = left_lane, -200

#damage
    if goku_loc[0] == mob_loc[0] and mob_loc[1] == goku_loc[1]:
        print('game over')
        break

    #event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                goku_loc = goku_loc.move ([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                goku_loc = goku_loc.move ([int(road_w/2), 0])
    pygame.draw.rect(
        screen,
        (50,50,50),
        (width/2-road_w/2, 0, road_w, height)
    )

    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - roadmark_w/2, 0, roadmark_w, height)
    )
    screen.blit(goku, goku_loc)
    screen.blit(mob, mob_loc)
    pygame.display.update()

pygame.quit()