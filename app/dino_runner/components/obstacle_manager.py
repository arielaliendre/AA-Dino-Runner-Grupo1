from random import randint
from dino_runner.components.cactus import Cactus
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager():

    def __init__(self):
        self.obstacles = []

    def update(self):
        if len(self.obstacles) == 0:
            index_random = randint(0, 2)
            self.obstacles.append(self.generate_obstacle(index_random))

        for obstacle in self.obstacles:
            obstacle.update(15, self.obstacles)

    def generate_obstacle(self, index):
        if index == 0:
            return Cactus(SMALL_CACTUS, 320)
        elif index == 1:
            return Cactus(LARGE_CACTUS, 295)
        elif index == 2:
            return Bird(BIRD)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)