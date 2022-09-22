import pygame



class Character:
    def __init__(self, start_pos, image):
        self.pos = start_pos
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.currentX, self.currentY = start_pos

    def move_up(self):
        self.currentX +=1
        self.update()

    def move_down(self):
        self.currentX += -1
        self.update()

    def move_left(self):
        self.currentY += 1
        self.update()

    def move_right(self):
        self.currentY += -1
        self.update()

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        self.update()

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)