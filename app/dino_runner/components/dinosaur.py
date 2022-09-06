from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import DUCKING

class Dinosaur(Sprite):

    X_POS = 50
    Y_POS = 300

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.first_image = True
        self.action = 0

    def update(self):
        if self.action == 0:
            self.run()

        self.step_index += 1

    def run(self):
        if self.step_index % 6 == 0:
            self.first_image = not self.first_image

        if self.first_image:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]

    def down(self):
        if self.step_index % 6 == 0:
            self.first_image = not self.first_image

        if self.first_image:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]

        self.action = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))