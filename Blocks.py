from Entity import Entity
import pygame
from Settings import RED, BLACK, BLUE, WHITE

class Block(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.collidable = True

    def draw(self, screen, camera):
        pos = camera.translate(self)
        if pos is None:
            return
        #box = pygame.Rect(pos[0], pos[1], pos[0] + blocksize, pos[1] + blocksize)
        box = camera.translate(self)
        pygame.draw.rect(screen, RED, box, 2)

    def colliding(self, other):
        if self.collidable:
            return super().colliding(other)
        return False, 0, 0

class Entry(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.collidable = False

class Exit(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.collidable = False
        self.nextLevel = None


class Floor(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.collidable = True

    def draw(self, screen, camera):
        pos = camera.translate(self)
        if pos is None:
            return
        box = camera.translate(self)
        pygame.draw.rect(screen, BLACK, box, 2)


class Wall(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.collidable = True

    def draw(self, screen, camera):
        pos = camera.translate(self)
        if pos is None:
            return
        box = camera.translate(self)
        pygame.draw.rect(screen, BLUE, box, 2)


class Empty(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.collidable = False

    def draw(self, screen, camera):
        pos = camera.translate(self)
        if pos is None:
            return
        box = camera.translate(self)
        pygame.draw.rect(screen, WHITE, box, 2)