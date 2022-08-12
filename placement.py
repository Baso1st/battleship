from abc import ABC, abstractmethod
import random
from typing import List
from ship import Ship


class CellState:
    Empty = 0
    Has_Ship = 1
    Miss = 2
    Hit = 3

class Cell:
    def __init__(self) -> None:
        self.state = CellState.Empty
        self.ship = None

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
        board = [[Cell() for j in range(self._col_count)] for i in range(self._row_count)]

        for ship in self._ships:
            coords = self._get_coords(ship.size, board)
            for r, c in coords: 
                board[r][c].state = CellState.Has_Ship
                board[r][c].ship = ship
        return board


    def _get_coords(self, size, board):
        """
        This method returns a randome location to place the ship. 
        It choses a random cell and direction, then checks if the ship size fits there, if not it tries with a different cell. 
        """
        good_cells = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].state == CellState.Empty:
                    good_cells.add((i, j))

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
                    if len(coords) == size:
                        return coords
                else:
                    for k in range(i, i + size):
                        if (k, j) in good_cells:
                            coords.add((k, j))
                        else:
                            break
                    if len(coords) == size:
                        return coords
            good_cells.remove((i, j))
        
        raise Exception("Ship cannot be placed!!!")

class ManualPlacement(IShipPlacementStrategy):
    def place_ships(self):
        board = [[Cell() for j in range(self._col_count)] for i in range(self._row_count)]

        stack = list(self._ships)
        while stack:
            ship = stack.pop()
            self._print_board(board)
            coords = input(f"Where would you like to place {ship} of size {ship.size}?\n"
                         f"Start Cell (ex: 0, 3): ")
            r, c = [int(i) for i in coords.split(',')]
            direction = int(input(f"Direction? 1 for Vertical and 2 for Horizontal? "))
            if self._is_valid_placement(r, c, direction, board, ship.size):
                self._place_ship(r, c, direction, board, ship)
            else:
                print("Can't place the ship in that location and direction. Please try again")
                stack.append(ship)

        return board

    def _print_board(self, board):
        for row in board:
            cell_states = [cell.state for cell in row] #ToDo: Add some colors to make it clear what's what
            print(cell_states)
    
    def _is_valid_placement(self, r, c, direction, board, ship_size):
        if direction == Direction.Horizontal:
            for i in range(c, c + ship_size):
                if board[r][i].state != CellState.Empty:
                    return False
        elif direction == Direction.Vertical:
            for i in range(r, r + ship_size):
                if board[i][c].state != CellState.Empty:
                    return False
        else:
            return False
        
        return True

    def _place_ship(self, r, c, direction, board, ship):
        if direction == Direction.Horizontal:
            for i in range(c, c + ship.size):
                board[r][i].state = CellState.Has_Ship
                board[r][i].ship = ship
        elif direction == Direction.Vertical:
            for i in range(r, r + ship.size):
                board[i][c].state = CellState.Has_Ship
                board[i][c].ship = ship
        else:
            raise ValueError("Incorrect Direction")


