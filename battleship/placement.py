from abc import ABC, abstractmethod
import random
from typing import List
from ship import Ship


class Direction:
    Vertical = 1
    Horizontal = 2

class ShipLocation:
    def __init__(self, i, j, direction):
        self.i = i
        self.j = j
        self.direction = direction


class IShipPlacementStrategy(ABC):
    def __init__(self, ships: List[Ship], row_count, col_count) -> None:
        self._ships = ships
        self._row_count = row_count
        self._col_count = col_count

    @abstractmethod
    def place_ships(self) -> dict:
        pass

class AutoPlacement(IShipPlacementStrategy):
    def place_ships(self):
        board = {}
        available_cells = set()
        for i in range(self._row_count):
            for j in range(self._col_count):
                available_cells.add((i, j))
        for ship in self._ships:
            coords = self._get_coords(ship.size, available_cells)
            for coord in coords: 
                board[coord] = ship
                available_cells.remove(coord)
        return board


    def _get_coords(self, size, available_cells):
        """
        This method returns a randome location to place the ship. 
        It choses a random cell and direction, then checks if the ship size fits there, if not it tries with a different cell. 
        """
        good_cells = set(available_cells)
        while len(good_cells) > size:
            i, j = random.choice(tuple(good_cells))
            dir_list = [Direction.Horizontal, Direction.Vertical]
            random.shuffle(dir_list)
            for dir in dir_list:
                coords = set()
                if dir == Direction.Horizontal:
                    for k in range(j, j + size):
                        if (i, k) in good_cells:
                            coords.add((i, k))
                        else:
                            break
                    return coords
                else:
                    for k in range(i, i + size):
                        if k in good_cells:
                            coords.add((k, j))
                        else:
                            break
                    return coords
            good_cells.remove((i, j))
        
        raise Exception("Ship cannot be placed!!!")


# class ManualPlacement(IShipPlacementStrategy):

#     def place_ships(self, ships: List[Ship], board):
#         row_count = len(board)
#         col_count = board[0]
#         available_rows = [i for i in range(row_count)]
#         available_cols = [i for i in range(len(col_count))]
#         for ship in ships:
#             coords = self._get_coords(ship.size, available_rows, available_cols)
#             for coord in coords: 
#                 board[coord] = ship

#     def _get_coords(self, size, shipDirection):
#         coords = []
#         for idx in range(size):
#             if shipDirection.direction == Direction.Vertical:
#                 coords.append((shipDirection.i + idx, shipDirection.j))
#             else:
#                 coords.append((shipDirection.i, shipDirection.j + idx))
#         return coords
