#!/usr/bin/env python3
from typing import List

import pygame
from sprite import Sprite, Side
from random import choice

SIZE = 800
CELL_SIZE = 40
window = pygame.display.set_mode((SIZE, SIZE))
caption = "Hello Pygame!"
pygame.display.set_caption(caption)

screen = pygame.Surface((SIZE, SIZE))


class Snake:
    def __init__(self, x_pos, y_pos, filename):
        self.x = x_pos
        self.y = y_pos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))
        self.tail: List[Sprite] = []
        self.length = 3
        self.side = [Side.RIGHT]

    def render(self, surface_to_render):
        surface_to_render.blit(self.bitmap, (self.x, self.y))
        if self.tail:
            for each_cell in self.tail[1:]:
                each_cell.render(surface_to_render=screen)

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
        self.tail.insert(0, Sprite(self.x, self.y, 'zet.png'))
        while len(self.tail) > self.length:
            self.tail.pop()
        count = 0
        for each_cell in self.tail:
            count += 1
            each_cell.number = count

    def len(self):
        # Calling of this method is making the snake longer by 1 pt
        self.length += 1


coords = range(0, SIZE - CELL_SIZE, CELL_SIZE)
hero = Snake(choice(coords), choice(coords), 'zet.png')
zet = Sprite(choice(coords), choice(coords), 'hero.png')

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if (e.key == pygame.K_d or e.key == pygame.K_RIGHT) and hero.side[-1] != 3:
                hero.turn_to(Side.RIGHT)
            elif (e.key == pygame.K_s or e.key == pygame.K_DOWN) and hero.side[-1] != 4:
                hero.turn_to(Side.DOWN)
            elif (e.key == pygame.K_a or e.key == pygame.K_LEFT) and hero.side[-1] != 1:
                hero.turn_to(Side.LEFT)
            elif (e.key == pygame.K_w or e.key == pygame.K_UP) and hero.side[-1] != 2:
                hero.turn_to(Side.UP)

    screen.fill((5, 5, 5))
    zet.render(surface_to_render=screen)
    hero.move()
    if hero.check_collision(zet):
        zet.x = choice(coords)
        zet.y = choice(coords)
        hero.len()
    #  TODO: To be moved into snake itself
    for each in hero.tail[1:]:
        if each.x == hero.x and each.y == hero.y:
            hero.length = each.number
    hero.render(surface_to_render=screen)
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(300)
    if hero.length <= 1:
        caption = "Hello Pygame"
    else:
        caption = "Your score is %d" % (hero.length - 1)
    pygame.display.set_caption(caption)
