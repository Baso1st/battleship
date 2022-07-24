from abc import ABC, abstractmethod
from typing import List
from battleshipgame import *
from placement import *
from ship import *
from player import *


def get_ships(player):
    prefix = 'USS' if player == 1 else 'Alien'
    return[
        AirCraftCarrier(f"{prefix} Thunder"),
        Destroyer(f"{prefix} Navy Pride"),
        Destroyer(f"{prefix} Navigator"),
        SmallBoat(f"{prefix} boat1"),
        SmallBoat(f"{prefix} boat2"),
        SmallBoat(f"{prefix} boat3"),
        SmallBoat(f"{prefix} boat4"),
        Submarine(f"{prefix} Silent Hunter"),
        Submarine(f"{prefix} Whisperer"),
        Submarine(f"{prefix} Sea snake")
    ]


if __name__== '__main__':
    row_count = 10
    col_count = 10
    player_count = int(input("How many players?"))
    players = []
    for i in range(player_count):
        ships = get_ships(i+1)
        name = input(f"Player {i+1} please enter your name:")
        human = Human(name, AutoPlacement(ships, row_count, col_count))
        human.place_ships()
        players.append(human)
    if player_count == 1:
        ships = get_ships(float('inf'))
        ai = AI('Computer', AutoPlacement(ships, row_count, col_count))
        ai.place_ships()
        players.append(ai)
    
    game = BattleShipGame(players)

    round = 0

    human_cells = []
    computer_cells = []
    for i in range(row_count):
        for j in range(col_count):
            human_cells.append((i, j))
            computer_cells.append((i, j))

    while not game.has_winner():
        if round % 2 == 0:
            offensive, defensive = players[0], players[1]
            i, j = random.choice(human_cells)
            human_cells.remove((i,j))
            # (i, j) = [int(x) for x in input(f"{offensive.name} please enter your x y coordinates?").split()]
        else:
            offensive, defensive = players[1], players[0]
            i, j = random.choice(computer_cells)
            computer_cells.remove((i,j))

        hit_report = game.fire(offensive, defensive, (i, j))
        print(f"{offensive.name} played ({i}, {j}): {hit_report}")

        round += 1
    
    print(f"Congratulaton player {game.winner.name}, you have own!!!")
    print(f"Played Rounds: {round}")