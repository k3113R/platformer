import pygame as pg


class Entity:
    def __init__(self, x, y):
        self.sprite = None
        self.collidable = False
        self.x = x
        self.y = y
        self.height = 1
        self.width = 1
        self.rect = pg.Rect(x, y, 1, 1)

    # def tick(self, timePassed):
    #     pass
    #
    # def draw(self, canvas, camera):
    #     pass
    
    # def collision_test(self, rect, grid):
    #     hit_list = []
    #     for row in grid:
    #         for block in row:
    #             if block.collidable and block.rect.colliderect(rect):
    #                 hit_list.append(block)
    #     return hit_list
    def collision_test(self, grid):
        for row in grid:
            for block in row:
                r, self.x, self.y = block.colliding(self)
        return r, self.x, self.y

    #other is the one moving
    def colliding(self, other):
        self_top = self.y
        self_bot = self.y + self.height
        other_top = other.y
        other_bot = other.y + other.height
        self_left = self.x
        self_right = self.x + self.width
        other_left = other.x
        other_right = other.x + self.width
        newY = other.y
        newX = other.x
        colliding = False

        if self_top <= other_bot <= self_bot:
            colliding = True
            newY = self_top - other.height

        if self_top <= other_top <= self_bot:
            colliding = True
            newY = self_bot

        if self_left <= other_right <= self_right:
            colliding = True
            newX = self_left - other.width

        if self_left <= other_left <= self_right:
            colliding = True
            newX = self_right
        #print(colliding, newY, newX)
        return colliding, newY, newX

