from abc import ABC, abstractmethod

from placement import CellState, Cell, IShipPlacementStrategy


class HitEffect:
    def __init__(self, is_hit: bool, hit_report: str):
        self.is_hit = is_hit
        self.hit_report = hit_report

class Player(ABC):
    def __init__(self, name, shipPlacementStrategy: IShipPlacementStrategy) -> None:
        self._board = []
        self._shipPlacementStrategy = shipPlacementStrategy
        self.name = name
        self._score = 0
        self._hits = 0
        
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def hits(self):
        return self._hits


    def place_ships(self):
        self._board = self._shipPlacementStrategy.place_ships()

    def has_ships(self):
        #ToDo: This could be changed to track the number of ships through a class variable in a O(1) instead of O(n) like below
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                if self._board[i][j].state == CellState.Has_Ship:
                    return True
        return False
    
    def take_hit(self, coord):
        r, c = coord
        cell = self._board[r][c]
        if cell.state == CellState.Has_Ship:
            ship = cell.ship
            hit_report = ship.take_hit()
            self._hits += 1
            cell.state = CellState.Hit
            return HitEffect(True, hit_report)
        else:
            cell.state = CellState.Miss
            return HitEffect(False, 'Missed!!!')
    
    def get_unhit_cells(self):
        unhit_cells = []
        unhit_states = (CellState.Empty, CellState.Has_Ship)
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                if self._board[i][j].state in unhit_states:
                    unhit_cells.append((i, j))
        return unhit_cells

class Human(Player):
    pass
                
class AI(Player):
    pass
