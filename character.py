import pygame



class Character:
    def init(self, start_pos, image, rect):
        self.pos = start_pos
        self.image = pygame.image.load(image)
        self.update = self.rect = self.image.get_rect(topleft=self.pos)

    def move_up(self):
        self.pos[1] += 1

    def move_down(self):
        self.pos[1] += -1

    def move_left(self):
        self.pos[0] += 1

    def move_right(self):
        self.pos[0] += -1

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)