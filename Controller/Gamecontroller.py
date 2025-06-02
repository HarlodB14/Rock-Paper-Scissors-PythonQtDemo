import random

from model.Game import Game
from model.Move import Move
from model.Player import Player


class Gamecontroller:
    def __init__(self):
        self.winner = None
        self.moves = Move()
        self.game = Game()
        self.game.player = None
        self.ai_move = None

    def getplayer(self):
        return self.game.player

    def set_player(self, name):
        self.game.set_player(name)

    def get_moves(self):
        return self.moves.get_moves()

    def set_player_move(self, move):
        if self.game.player:
            self.game.player.move = move

    def get_player_move(self):
        return self.game.player.move

    def get_ai_move(self):
        if self.ai_move is None:
            self.ai_move = random.choice(self.moves.get_moves())
        return self.ai_move

    def determine_winner(self, player_move, ai_move):
        rules = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }
        if player_move == ai_move:
            self.winner = "Tie"
            return self.winner
        elif rules[player_move] == ai_move:
            self.winner = "Player"
            return self.winner
        else:
            self.winner = "AI"
            return self.winner

    def get_winner_name(self):
        return self.winner  # should return "Player", "AI", or "Gelijkspel"
