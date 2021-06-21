import enum

import pygame


class Side(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Sprite:
    def __init__(self, x_pos, y_pos, filename):
        self.x = x_pos
        self.y = y_pos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))

    def render(self, surface_to_render):
        surface_to_render.blit(self.bitmap, (self.x, self.y))
