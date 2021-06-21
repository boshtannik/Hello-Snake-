from abc import ABC

import pygame

from src.game_object_type import GameObjectType


class Sprite(ABC):
    def __init__(self, x_pos, y_pos, filename):
        self.x = x_pos
        self.y = y_pos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))
        self.type = GameObjectType.NONE

    def render(self, surface_to_render):
        surface_to_render.blit(self.bitmap, (self.x, self.y))