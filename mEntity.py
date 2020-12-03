from Entity import Entity


class MovingEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.movingLeft = False
        self.movingRight = False
        self.jumping = False
        self.grounded = False
        self.fallingVelocity = 0
        self.currentXvelocity = 0
        self.currentYvelocity = 0
        self.maxXvelocity = 0.5
        self.maxYvelocity = .5
        self.xAcceleration = .1
        self.yAcceleration = .2

    def update(self, level):
        if self.movingLeft:
            self.currentXvelocity -= self.xAcceleration
            self.currentXvelocity = max(self.currentXvelocity, -self.maxXvelocity)
        if self.movingRight:
            self.currentXvelocity += self.xAcceleration
            self.currentXvelocity = min(self.currentXvelocity, self.maxXvelocity)
        if not self.movingRight and not self.movingLeft:
            self.currentXvelocity /= 3.0

        if self.jumping and self.grounded:
            self.currentYvelocity = +self.maxYvelocity
            self.grounded = False
            self.jumping = False
        self.currentYvelocity -= self.yAcceleration
        self.currentYvelocity = min(self.currentYvelocity, self.maxYvelocity)
        self.y = self.y + self.currentYvelocity
        self.x = self.x + self.currentXvelocity
        colliders = self.collision_test(level)
        self.grounded = colliders[0]

    def move(self, timeDelta):
        nextX = self.x
        nextY = self.y
        if self.movingLeft:
            self.currentXvelocity -= self.xAcceleration
        if self.movingRight:
            self.currentXvelocity += self.xAcceleration
        