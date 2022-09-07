import random
from dino_runner.components.obstacle import Obstacle

class Cactus(Obstacle):

    def __init__(self, image, y):
        super().__init__(image, random.randint(0,2))
        self.rect.y = y