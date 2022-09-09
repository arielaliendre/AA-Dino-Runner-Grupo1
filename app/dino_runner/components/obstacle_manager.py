import pygame

from random import randint

from dino_runner.components.cactus import Cactus
from dino_runner.components.shield import Shield
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.dinosaur.dino_rect.colliderect(obstacle.rect):
                if game.dinosaur.type == SHIELD_TYPE:
                    game.dinosaur.type = DEFAULT_TYPE
                    self.obstacles.pop()
                    game.powerup_manager.active = 0
                    game.powerup_manager.time = 0
                elif game.dinosaur.type == HAMMER_TYPE:
                    self.obstacles.pop()
                else:
                    if game.hearts > 1:
                        game.hearts -= 1
                        self.obstacles.pop()
                    else:
                        pygame.time.delay(500)
                        game.playing = False

    def generate_obstacle(self):
        index_random = randint(0, 2)

        if index_random == 0:
            return Cactus(SMALL_CACTUS, 320)
        elif index_random == 1:
            return Cactus(LARGE_CACTUS, 295)
        elif index_random == 2:
            return Bird(BIRD, randint(80, 300))

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles.clear()