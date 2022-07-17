from abc import ABC

class Direction:
    Vertical = 1
    Horizontal = 2

class ShipPlacement:
    def __init__(self, i, j, direction):
        self.i = i
        self.j = j
        self.direction = direction

class Ship(ABC):
    def __init__(self, name, size):
        self.name = name
        self._size = size

    @property
    def size(self):
        return self._size

    def take_hit(self):
        self._size -= 1
        return self.get_hit_report()

    def get_hit_report(self):
        message = f"{type(self).__name__} {self.name} "
        if self._size > 0:
            return message + f"is criticaly hit. Remaining health: {self._size}"
        else:
            return message + f"has been destroyed"

class AirCraftCarrier(Ship):
    def __init__(self, name):
        super().__init__(name, 5)

class Destroyer(Ship):
    def __init__(self, name):
        super().__init__(name, 3)

class SmallBoat(Ship):
    def __init__(self, name):
        super().__init__(name, 1)

class Submarine(Ship):
    def __init__(self, name):
        super().__init__(name, 2)

class BattleShipGame:
    def __init__(self):
        self.boards = [None, {}, {}]
        self.winner = 0

    def place_ship(self, player, ship, shipPlacement):
        coords = self._get_coords(ship.size, shipPlacement)
        board = self.boards[player]
        for coord in coords: 
            board[coord] = ship

    def _get_coords(self, size, shipPlacement):
        coords = []
        for idx in range(size):
            if shipPlacement.direction == Direction.Vertical:
                coords.append((shipPlacement.i + idx, shipPlacement.j))
            else:
                coords.append((shipPlacement.i, shipPlacement.j + idx))
        return coords

    def hit(self, coord, player):
        #Basic input validation.
        other_player = 2 if player == 1 else 1
        board = self.boards[other_player]
        if coord in board:
            ship = board.pop((i, j))
            hit_effect = ship.take_hit()
            if not board:
                self.winner = player
            return hit_effect
        else:
            return "You missed! Big splash of water"


if __name__== '__main__':
    game = BattleShipGame()

    print("Seting up player 1 ships")

    game.place_ship(1, AirCraftCarrier("USS Thunder"), ShipPlacement(0, 0, Direction.Horizontal))
    game.place_ship(1, Destroyer("USS Navy Pride"), ShipPlacement(1, 0, Direction.Horizontal))
    game.place_ship(1, Destroyer("USS Navigator"), ShipPlacement(2, 0, Direction.Horizontal))
    game.place_ship(1, SmallBoat("USS boat1"), ShipPlacement(3, 0, Direction.Horizontal))
    game.place_ship(1, SmallBoat("USS boat2"), ShipPlacement(4, 0, Direction.Horizontal))
    game.place_ship(1, SmallBoat("USS boat3"), ShipPlacement(5, 0, Direction.Horizontal))
    game.place_ship(1, SmallBoat("USS boat4"), ShipPlacement(6, 0, Direction.Horizontal))
    game.place_ship(1, Submarine("USS Silent Hunter"), ShipPlacement(7, 0, Direction.Horizontal))
    game.place_ship(1, Submarine("USS Whisperer"), ShipPlacement(8, 0, Direction.Horizontal))
    game.place_ship(1, Submarine("USS Sea snake"), ShipPlacement(9, 0, Direction.Horizontal))

    print("Seting up player 2 ships")

    game.place_ship(2, AirCraftCarrier("Alien Thunder"), ShipPlacement(0, 0, Direction.Vertical))
    game.place_ship(2, Destroyer("Alien Navy Pride"), ShipPlacement(1, 0, Direction.Vertical))
    game.place_ship(2, Destroyer("Alien Navigator"), ShipPlacement(2, 0, Direction.Vertical))
    game.place_ship(2, SmallBoat("Alien boat1"), ShipPlacement(3, 0, Direction.Vertical))
    game.place_ship(2, SmallBoat("Alien boat2"), ShipPlacement(4, 0, Direction.Vertical))
    game.place_ship(2, SmallBoat("Alien boat3"), ShipPlacement(5, 0, Direction.Vertical))
    game.place_ship(2, SmallBoat("Alien boat4"), ShipPlacement(6, 0, Direction.Vertical))
    game.place_ship(2, Submarine("Alien Silent Hunter"), ShipPlacement(7, 0, Direction.Vertical))
    game.place_ship(2, Submarine("Alien Whisperer"), ShipPlacement(8, 0, Direction.Vertical))
    game.place_ship(2, Submarine("Alien Sea snake"), ShipPlacement(9, 0, Direction.Vertical))

    print('Thank you for placing your ships, Beign the battle! May the odds be in your favor')

    round = 0

    while not game.winner:
        if round % 2 == 0:
            player = 1
        else:
            player = 2
        
        (i, j) = [int(x) for x in input(f"Player {player} where do you hit?").split()]

        print(game.hit((i, j), player))

        round += 1
    
    print(f"Congratulaton player {game.winner}, you have own!!!")