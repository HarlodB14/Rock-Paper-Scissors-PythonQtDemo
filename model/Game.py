from model.Player import Player


class Game:
    player = None

    def __init__(self):
        self.player = None

    def set_player(self, name):
        self.player = Player(name, score=0, move=None)


