
class Direction:
    Vertical = 1
    HORIZONTAL = 2


class ShipPlacement:
    def __init__(self, i, j, direction):
        self.i = i
        self.j = j
        self.direction = direction


class Ship:
    def __init__(self, size, shipPlacement):
        #self.name = name
        self._size = size
        self._status = 1
        self._build_coordinates(size, shipPlacement)
    
    def _build_coordinates(self, size, shipPlacement):
        coords = []
        for idx in range(size):
            if shipPlacement.direction == Direction.Vertical:
                coords.append((shipPlacement.i, shipPlacement.j + idx))
            else:
                coords.append((shipPlacement.i + idx, shipPlacement.j))
        self.coordinates = coords


    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coords):
        self._coordinates = coords

    def take_hit(self, i, j):
        self.coordinates.remove((i, j))
        self._size -= 1
        if self._size == 0:
            self._status = 0
    
    def is_destroyed(self):
        return self._status == 0

    def get_public_info(self):
        return f"Ship Type: {type(self).__name__} is criticaly hit. Remaining health: {self._size}"

# class AirCraftCarrier(Ship):
#     def __init__(self, name):
#         super().__init__(name)
#         self.size = 5



class BattleShipGame:
    def __init__(self):
        self.player_one_ships = []
        self.player_two_ships = []
        self.winner = 0


    def place_ship(self, player, ship):
        if player == 1:
            self.player_one_ships.append(ship)
        else:
            self.player_two_ships.append(ship)


    def hit(self, i, j, player): # Refactor for performance
        ships = self.player_one_ships if player == 2 else self.player_two_ships
        hit_ship = None
        for ship in ships:
            if (i, j) in ship.coordinates:
                hit_ship = ship
                hit_ship.take_hit(i, j)
                break

        if hit_ship:
            if hit_ship.is_destroyed():
                ships.remove(hit_ship)

            if not ships:
                self.winner == player

            return hit_ship.get_public_info()
        else:
            return f"You missed!"


if __name__== '__main__':
    # 1 AirCraftCarrier size  5
    # 2 destroyers size  3
    # 4 small boat size  1
    # 3 Submarines size  2

    game = BattleShipGame()

    print(f"Player 1: Please send your ship locations, don't worry this information will be a secret ;)")

    game.place_ship(1, Ship(5, ShipPlacement(0, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(3, ShipPlacement(1, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(3, ShipPlacement(2, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(1, ShipPlacement(3, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(1, ShipPlacement(4, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(1, ShipPlacement(5, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(1, ShipPlacement(6, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(2, ShipPlacement(7, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(2, ShipPlacement(8, 0, Direction.HORIZONTAL)))
    game.place_ship(1, Ship(2, ShipPlacement(9, 0, Direction.HORIZONTAL)))

    print(f"Player 2: Please send your ship locations, don't worry this information will be a secret ;)")

    game.place_ship(2, Ship(5, ShipPlacement(0, 0, Direction.Vertical)))
    game.place_ship(2, Ship(3, ShipPlacement(0, 1, Direction.Vertical)))
    game.place_ship(2, Ship(3, ShipPlacement(0, 2, Direction.Vertical)))
    game.place_ship(2, Ship(1, ShipPlacement(0, 3, Direction.Vertical)))
    game.place_ship(2, Ship(1, ShipPlacement(0, 4, Direction.Vertical)))
    game.place_ship(2, Ship(1, ShipPlacement(0, 5, Direction.Vertical)))
    game.place_ship(2, Ship(1, ShipPlacement(0, 6, Direction.Vertical)))
    game.place_ship(2, Ship(2, ShipPlacement(0, 7, Direction.Vertical)))
    game.place_ship(2, Ship(2, ShipPlacement(0, 8, Direction.Vertical)))
    game.place_ship(2, Ship(2, ShipPlacement(0, 9, Direction.Vertical)))

    print('Thank you for placing your ships, Beign the battle! May the odds be in your favor')

    round = 0

    while not game.winner:
        if round % 2 == 0:
            player = 1
        else:
            player = 2
        
        (i, j) = [int(x) for x in input(f"Player {player} where do you hit?").split()]

        print(game.hit(i, j, player))

        round += 1
    
    print(f"Congratulaton player {game.winner}, you have own!!!")