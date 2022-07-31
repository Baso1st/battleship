from typing import List
from player import Player
from wining import IWinStrategy

class BattleShipGame:
    def __init__(self, players: List[Player], win_strategy: IWinStrategy):
        self._winner = None
        self._players = list(players)
        self._win_strategy = win_strategy

    def has_winner(self) -> bool:
        self._winner = self._win_strategy.get_winner(self._players)
        if self._winner:
            return True
        return False

    @property
    def winner(self) -> Player:
        return self._winner

    def fire(self, offensive_player: Player, defensive_player: Player, coord):
        hit_effect = defensive_player.take_hit(coord)
        if hit_effect.is_hit:
            offensive_player.score += 1
            if not defensive_player.has_ships():
                self._players.remove(defensive_player) #ToDo: Notify everyone that, this player is out.
        return hit_effect.hit_report

    def get_next_player(self):
        player = self._players.pop(0)
        self._players.append(player)
        return player