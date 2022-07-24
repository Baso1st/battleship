from typing import List
from player import Player


class BattleShipGame:
    def __init__(self, players: List[Player]):
        self._winner = None
        self.players = players

    def has_winner(self) -> bool:
        return self._winner != None

    @property
    def winner(self) -> Player:
        return self._winner

    def fire(self, offensive_player: Player, defensive_player: Player, coord):
        """
        ToDo: The function only supports two players for now. It needs to be changed.
        """
        hit_effect = defensive_player.take_hit(coord)
        if hit_effect.is_hit:
            offensive_player.score += 1
            if not defensive_player.has_ships():
                self._winner = offensive_player
        return hit_effect.hit_report