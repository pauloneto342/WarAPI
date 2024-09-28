from player import Player

class PlayerBuilder:
    def __init__(self, name):
        self.player = Player(name)

    def set_color(self, color):
        self.player.set_color(color)
        return self

    def set_army(self, size):
        self.player.add_army(size)
        return self

    def set_objective(self, task):
        self.player.set_objective(task)
        return self

    def build(self):
        return self.player
