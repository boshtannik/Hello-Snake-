#!/usr/bin/env python3
import pygame

from config import SIZE, WINDOW_NAME, CELL_SIZE
from sprite import Sprite
from snake import Snake, Side
from random import choice

window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption(WINDOW_NAME)

screen = pygame.Surface((SIZE, SIZE))


coordinates = range(0, SIZE - CELL_SIZE, CELL_SIZE)
hero = Snake(choice(coordinates), choice(coordinates), 'zet.png')
zet = Sprite(choice(coordinates), choice(coordinates), 'hero.png')

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if (e.key == pygame.K_d or e.key == pygame.K_RIGHT) and hero.side[-1] != Side.LEFT:
                hero.turn_to(Side.RIGHT)
            elif (e.key == pygame.K_s or e.key == pygame.K_DOWN) and hero.side[-1] != Side.UP:
                hero.turn_to(Side.DOWN)
            elif (e.key == pygame.K_a or e.key == pygame.K_LEFT) and hero.side[-1] != Side.RIGHT:
                hero.turn_to(Side.LEFT)
            elif (e.key == pygame.K_w or e.key == pygame.K_UP) and hero.side[-1] != Side.DOWN:
                hero.turn_to(Side.UP)

    screen.fill((5, 5, 5))
    zet.render(surface_to_render=screen)
    hero.move()
    if hero.check_collision(zet):
        zet.x = choice(coordinates)
        zet.y = choice(coordinates)
        hero.len()
    #  TODO: To be moved into snake itself
    for each_cell in hero.tail[1:]:
        if each_cell.x == hero.x and each_cell.y == hero.y:
            hero.length = each_cell.number
    hero.render(surface_to_render=screen)
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(300)
    if hero.length <= 1:
        caption = "Hello Pygame"
    else:
        caption = "Your score is %d" % (hero.length - 1)
    pygame.display.set_caption(caption)
