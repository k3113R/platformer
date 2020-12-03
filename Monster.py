from Entity import Entity

class Monster(Entity):
    def __init__(self):
        self.hp = 10
        self.name = "monster"


class FlyingMonster(Monster):
    def __init__(self):
        super().__init__()
        self.gravity = 0


class Yeti(Monster):
    def __init__(self):
        super().__init__()
        self.hp = 20