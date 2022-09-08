import random
from dino_runner.components.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image, y):
        super().__init__(image, 0)
        self.rect.y = y
        self.step_index = 0

    def update(self, obstacle_speed, obstacles):
        super().update(obstacle_speed, obstacles)
        
        self.index = (self.step_index % 10) // 5
        self.step_index += 1
