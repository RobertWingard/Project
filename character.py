import pygame



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