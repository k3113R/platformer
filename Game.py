from Level import *
from Monster import *
from Player import *
from Blocks import *
from Items import *
from Settings import *
import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.running = False
        self.level = Level("levels/level0.txt")
        self.camera = Camera(0, 0)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.handleInput()
            self.tick()
            self.draw()

    def draw(self):
        self.screen.fill((120, 120, 120))
        self.level.draw(self.screen, self.camera)
        pygame.display.flip()

    def tick(self):
        self.level.update()
        self.camera.update(self.level.player)

    def handleInput(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


class Camera:
    def __init__(self, row, col):
        self.worldX = row
        self.worldY = col


    # def follow(self, target):
    #     self.x = target.x
    #     self.y = target.y
    #
    # def translate(self, entity):
    #     newx = entity.x - self.x
    #     newy = entity.y - self.y
    #     newx *= BLOCKSIZE
    #     newy *= BLOCKSIZE
    #     newx -= (WIDTH/2)
    #     newy -= (HEIGHT/2)
    #     print(newx, newy)
    #     if newx < 0 or newx > WIDTH or newy < 0 or newy > HEIGHT:
    #         return None
    #     return entity.rect.move(newx, newy)

    # def apply(self, entity):
    #     return entity.rect.move(self.camera.topleft)

    def translate(self, target):
        localX = target.x - self.worldX
        localY = target.y - self.worldY
        localX += (WIDTH / BLOCKSIZE) / 2
        localY += (HEIGHT / BLOCKSIZE) / 2
        left = localX * BLOCKSIZE
        top = localY * BLOCKSIZE
        width = BLOCKSIZE
        height = BLOCKSIZE
        return pygame.Rect(left, top, width, height)




    def update(self, target):

        self.worldX = target.x
        self.worldY = target.y
        # x = -target.rect.x + int(WIDTH / 2)
        # y = -target.rect.y + int(HEIGHT / 2)
        # #limit scrolling to map size
        # x = min(0, x) #left
        # y = min(0, y) #top
        # x = max(self.width - WIDTH, x) #right
        # y = max(self.height - HEIGHT, y) #bottom
        #
        # self.camera = pygame.Rect(x, y, self.width, self.height)


if __name__ == "__main__":
    g = Game()
    g.run()
    pygame.quit()