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
        self._score = 0
        self._hits = 0
        
        
    @abstractmethod
    def place_ships(self):
        pass

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def hits(self):
        return self._hits


    def has_ships(self):
        #ToDo: This could be changed to track the number of ships through a class variable in a O(1) instead of O(n) like below
        for ship in self._board.values():
            if ship:
                return True
        return False
    
    def take_hit(self, coord):
        ship = self._board.pop(coord)
        if ship:
            hit_report = ship.take_hit()
            self._hits += 1
            return HitEffect(True, hit_report)
        else:
            return HitEffect(False, 'Missed!!!')
    
    def get_unhit_cells(self):
        return list(self._board.keys())

class Human(Player):

    def place_ships(self):
        self._board = self._shipPlacementStrategy.place_ships()
                
class AI(Player):

    def place_ships(self):
        self._board = self._shipPlacementStrategy.place_ships()
