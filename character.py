import pygame
import random



class Character:
    def __init__(self, start_pos, image):
        self.pos = start_pos
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.currentX, self.currentY = start_pos

    def move_up(self):
        self.currentY += -10
        self.update()

    def move_down(self):
        self.currentY += 10
        self.update()

    def move_left(self):
        self.currentX += -10
        self.update()

    def move_right(self):
        self.currentX += 10
        self.update()

    def draw(self,screen):
        # screen_width = 1200
        # screen_height = 800
        # screen = pygame.display.set_mode((screen_width, screen_height))
        screen.blit(self.image, (self.currentX, self.currentY))
        self.update()


    def update(self):
        self.rect = self.image.get_rect(topleft=(self.currentX, self.currentY))


class Enemy:
    def __init__(self, start_pos, image):
        self.pos = start_pos
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.currentX, self.currentY = start_pos
        self.x = random.choice([0,1200])
        self.y = random.randint(100,800)
        if self.x == 0:
            self.direction = 'right'
        if self.x == 1200:
            self.direction = 'left'

    def move_up(self):
        self.currentY += -10
        self.update()

    def move_down(self):
        self.currentY += 10
        self.update()

    def move_left(self):
        self.currentX += -10
        self.update()

    def move_right(self):
        self.currentX += 10
        self.update()

    def draw(self,screen):
        # screen_width = 1200
        # screen_height = 800
        # screen = pygame.display.set_mode((screen_width, screen_height))
        if self.direction == 'right':
            self.x +=5
            if self.x > 1200:
                self.x = random.choice([0,1200])
                self.y = random.randint(100,800)
                if self.x == 0:
                    self.direction = 'right'
                if self.x == 1200:
                    self.direction = 'left'
                
        if self.direction == 'left':
            self.x +=-5
            if self.x < 0:
                self.x = random.choice([0,1200])
                self.y = random.randint(100,800)
                if self.x == 0:
                    self.direction = 'right'
                if self.x == 1200:
                    self.direction = 'left'
        screen.blit(self.image, (self.x, self.y))
        self.update()


    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))