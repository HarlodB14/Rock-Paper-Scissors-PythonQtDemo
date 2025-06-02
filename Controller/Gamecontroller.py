from model.Game import Game
from model.Player import Player


class Gamecontroller:
    def __init__(self):
        self.game = Game()
        self.game.player = None

    def getplayer(self):
        return self.game.player

    def set_player(self, name):
        self.game.set_player(name)
