from sre_constants import JUMP
from pygame.sprite import Sprite
import pygame

from dino_runner.utils.constants import DUCKING_HAMMER, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, RUNNING, DUCKING, DUCKING_SHIELD, RUNNING_HAMMER, RUNNING_SHIELD, JUMPING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE

class Dinosaur(Sprite):

    X_POS = 50
    Y_POS = 300

    Y_POS_DUCK = 335

    JUMP_VEL = 9

    RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
    JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
    DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = self.RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.state = 0
        self.jump_vel = self.JUMP_VEL

    def update(self, key_in):
        if self.state == 0:
            self.run()
        elif self.state == 1:
            self.duck()
        else:
            self.jump()

        if key_in[pygame.K_DOWN]:
            self.state = 1
            self.jump_vel = self.JUMP_VEL
        elif key_in[pygame.K_UP]:
            self.state = 2
        else:
            if self.state != 2:
                self.state = 0

        self.step_index += 1

    def run(self):
        self.image = self.RUN_IMG[self.type][(self.step_index % 10) // 5]
        self.dino_rect.y = self.Y_POS

    def duck(self):
        self.image = self.DUCK_IMG[self.type][(self.step_index % 10) // 5]
        self.dino_rect.y = self.Y_POS_DUCK

    def jump(self):
        self.image = self.JUMP_IMG[self.type]

        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 1

        if self.jump_vel < -self.JUMP_VEL:
            self.state = 0
            self.dino_rect.y = self.Y_POS
            self.jump_vel = self.JUMP_VEL

    def reset(self):
        self.type = DEFAULT_TYPE

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))