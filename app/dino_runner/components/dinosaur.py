from pygame.sprite import Sprite
import pygame

from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING

class Dinosaur(Sprite):

    X_POS = 50
    Y_POS = 300

    Y_POS_DUCK = 335

    JUMP_VEL = 9

    def __init__(self):
        self.image = RUNNING[0]
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
        self.image = RUNNING[(self.step_index % 10) // 5]
        self.dino_rect.y = self.Y_POS

    def duck(self):
        self.image = DUCKING[(self.step_index % 10) // 5]
        self.dino_rect.y = self.Y_POS_DUCK

    def jump(self):
        self.image = JUMPING

        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 1

        if self.jump_vel < -self.JUMP_VEL:
            self.state = 0
            self.dino_rect.y = self.Y_POS
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))