from abc import ABC, abstractmethod

from placement import IShipPlacementStrategy


class HitEffect:
    def __init__(self, is_hit: bool, hit_report: str):
        self.is_hit = is_hit
        self.hit_report = hit_report

class Player(ABC):
    def __init__(self, name, shipPlacementStrategy: IShipPlacementStrategy) -> None:
        self._board = {}
        self._shipPlacementStrategy = shipPlacementStrategy
        self.name = name
        self.score = 0
        
    @abstractmethod
    def place_ships(self):
        pass


    def has_ships(self):
        return len(self._board) > 0
    
    def take_hit(self, coord):
        if coord in self._board:
            ship = self._board[coord]
            hit_report = ship.take_hit()
            self._board.pop(coord)
            return HitEffect(True, hit_report)
        else:
            return HitEffect(False, 'Missed!!!')

class Human(Player):

    def place_ships(self):
        self._board = self._shipPlacementStrategy.place_ships()
                
class AI(Player):

    def place_ships(self):
        self._board = self._shipPlacementStrategy.place_ships()
