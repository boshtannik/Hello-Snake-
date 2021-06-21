import enum
from typing import List

import pygame

from src.cell import Cell
from config import CELL_SIZE, SIZE


class Side(enum.Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Snake:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.bitmap = pygame.image.load("src/zet.png")
        self.bitmap.set_colorkey((0, 0, 0))
        self.tail: List[Cell] = []
        self.length = 3
        self.side = [Side.RIGHT]

    def render(self, surface_to_render):
        surface_to_render.blit(self.bitmap, (self.x, self.y))
        if self.tail:
            for each_cell in self.tail[1:]:
                each_cell.render(surface_to_render=surface_to_render)

    def turn_to(self, got_side: Side):
        self.side.append(got_side)

    def check_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        if self.tail:
            for each_cell in self.tail[1:]:
                if each_cell.x == other.x and each_cell.y == other.y:
                    return True

    def update(self):
        if self.side[-1] == Side.RIGHT:
            self.x += CELL_SIZE
        elif self.side[-1] == Side.DOWN:
            self.y += CELL_SIZE
        elif self.side[-1] == Side.LEFT:
            self.x -= CELL_SIZE
        elif self.side[-1] == Side.UP:
            self.y -= CELL_SIZE
        if len(self.side) > 1:
            self.side.pop(0)

    def correct(self):
        if self.x > SIZE - CELL_SIZE:
            self.x = 0
        elif self.y > SIZE - CELL_SIZE:
            self.y = 0
        elif self.x < 0:
            self.x = SIZE - CELL_SIZE
        elif self.y < 0:
            self.y = SIZE - CELL_SIZE

    def move(self):
        self.update()
        self.correct()
        self.tail.insert(0, Cell(self.x, self.y, 'src/zet.png'))
        while len(self.tail) > self.length:
            self.tail.pop()
        count = 0
        for each_cell in self.tail:
            count += 1
            each_cell.number = count

    def len(self):
        # Calling of this method is making the snake longer by 1 pt
        self.length += 1
