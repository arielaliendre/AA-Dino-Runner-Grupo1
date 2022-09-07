import random
from dino_runner.components.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image):
        super().__init__(image, random.randint(0,1))
        self.rect.y = 250
        self.step_index = 0

    def update(self, obstacle_speed, obstacles):
        super().update(obstacle_speed, obstacles)
        
        self.index = (self.step_index % 10) // 5
        self.step_index += 1
