from typing import List
from player import Player


class BattleShipGame:
    def __init__(self, players: List[Player]):
        self._winner = None
        self._players = list(players)

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
                self._players.remove(defensive_player) # ToDo: Need to notify everyone that this player is out.
                if len(self._players) == 1:
                    self._winner = self._players[0]
        return hit_effect.hit_report

    def get_next_player(self):
        player = self._players.pop(0)
        self._players.append(player)
        return player