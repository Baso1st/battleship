from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List
from battleshipgame import *
from placement import *
from ship import *
from player import *


def get_ships(name):
    return[
        AirCraftCarrier(f"{name} Thunder"),
        Destroyer(f"{name} Navy Pride"),
        Destroyer(f"{name} Navigator"),
        SmallBoat(f"{name} boat1"),
        SmallBoat(f"{name} boat2"),
        SmallBoat(f"{name} boat3"),
        SmallBoat(f"{name} boat4"),
        Submarine(f"{name} Silent Hunter"),
        Submarine(f"{name} Whisperer"),
        Submarine(f"{name} Sea snake")
    ]


if __name__== '__main__':
    row_count = 10
    col_count = 10
    player_count = int(input("How many players?"))
    players = []
    for i in range(player_count):
        name = input(f"Player {i+1} please enter your name:")
        ships = get_ships(name)
        human = Human(name, AutoPlacement(ships, row_count, col_count))
        human.place_ships()
        players.append(human)
    if player_count == 1:
        name = 'Computer'
        ships = get_ships(name)
        ai = AI(name, AutoPlacement(ships, row_count, col_count))
        ai.place_ships()
        players.append(ai)
    
    game = BattleShipGame(players)

    round = 1
    while not game.has_winner():
        offensive = game.get_next_player()
        # defensive_number = int(input(f"{offensive.name} who would you like to attack?"))
        # defensive = players[defensive_number]
        defensive = random.choice([x for x in game._players if x != offensive])
        i, j = random.choice(defensive.get_unhit_cells()) # In a real situation a human will make their own choices.
        # (i, j) = [int(x) for x in input(f"{offensive.name} please enter your x y coordinates?").split()]

        hit_report = game.fire(offensive, defensive, (i, j))
        print(f"Round {round}: {offensive.name} played ({i}, {j}): {hit_report}")
        round += 1

    print(f"Congratulations {game.winner.name}, you have own!!!")