from mEntity import MovingEntity
import pygame as pg
from Settings import *


class Player(MovingEntity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vx = 0
        self.vy = 0
        self.height = .95
        self.width = .95
        self.grounded = False
        self.sprite = pg.image.load("graphics/Player.png").convert_alpha()

    def update(self, level):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.movingLeft = True
        else:
            self.movingLeft = False
        if keys[pg.K_RIGHT]:
            self.movingRight = True
        else:
            self.movingRight = False
        if keys[pg.K_UP] and self.grounded:
            self.jumping = True
        super().update(level.grid)



    def move(self, rect, movement, tiles):
        collision_types = {"top": False, "bottom": False, "right": False, "left": False}
        rect.x += movement[0]
        hit_list = rect.collision_test(tile)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = rect.collision_test(tile)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[0] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def draw(self, screen, camera):
        pos = camera.translate(self)
        if pos is None:
            return
        box = camera.translate(self)
        pg.draw.rect(screen, YELLOW, box)
        pg.Surface.blit(self.sprite, screen, box)

