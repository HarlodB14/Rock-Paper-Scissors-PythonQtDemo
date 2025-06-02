from model.Game import Game
from model.Move import Move
from model.Player import Player


class Gamecontroller:
    def __init__(self):
        self.moves = Move()
        self.game = Game()
        self.game.player = None

    def getplayer(self):
        return self.game.player

    def set_player(self, name):
        self.game.set_player(name)

    def get_moves(self):
        return self.moves.get_moves()

    def set_player_move(self, move):
        if self.game.player:
            self.game.player.move = move
