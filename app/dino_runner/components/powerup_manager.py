import pygame

from random import randint

from dino_runner.components.shield import Shield
from dino_runner.components.hammer import Hammer
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.time = 0
        self.active = False

    def update(self, game):
        if len(self.power_ups) == 0 and game.dinosaur.type == DEFAULT_TYPE:
            self.power_ups.append(self.generate_power_up())

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.dinosaur.dino_rect.colliderect(power_up.rect):
                game.dinosaur.type = power_up.type
                self.active = True

        if self.time > 200:
            game.dinosaur.type = DEFAULT_TYPE
            self.active = False
            self.time = 0

        if self.active:
            self.time += 1

    def generate_power_up(self):
        index_random = randint(0, 1)

        if index_random == 0:
            return Shield()
        elif index_random == 1:
            return Hammer()

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups.clear()