from Blocks import *
from Player import Player
class Level:
    def __init__(self, file=None):
        self.grid = []
        self.monsters = []
        self.items = []
        self.startX = 0
        self.startY = 0
        if file is not None:
            self.load(file)
        self.player = Player(self.startX, self.startY)

    def load(self, file):
        with open(file) as data:
            lineNum = 0
            for line in data:
                self.grid.append([])
                col = 0
                for char in line:
                    b = Empty(col, lineNum)
                    if char == "s":
                        b = Entry(col, lineNum)
                        # self.startX = b.x
                        # self.startY = b.y
                    if char == "x":
                        b = Floor(col, lineNum)
                    if char == "z":
                        b = Wall(col, lineNum)
                    self.grid[lineNum].append(b)
                    col += 1
                lineNum += 1

    def draw(self, screen, camera):
        for row in self.grid:
            for object in row:
                object.draw(screen, camera)
        self.player.draw(screen, camera)

    def update(self):
        self.player.update(self)

    def colliding(self, row, col, other):
        if row < 0:
            return True, 1, col
        if col < 0:
            return True, row, 1
        if row >= len(self.grid):
            return True, len(self.grid) - 2, col
        if col >= len(self.grid[row]):
            return True, row, len(self.grid[row]) - 2
        return self.grid[row][col].colliding(other)

    def physics_step(self):
        """
        for each moving entity
            if entity has moving left flag
                calculate position left
                if new position not colliding
                    change entity to new position
            if entity has moving right flag
                calculate position right
                if new position not colliding
                    change entity to new position
        Apply gravity by increasing falling velocity while in air
        :return:
        """
