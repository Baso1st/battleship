from abc import ABC, abstractmethod
from time import sleep
from typing import List
from battleshipgame import *
from placement import *
from ship import *
from player import *
from wining import *
import random


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
    print("*"*20 + "  Welcome To BattleShip  " + "*"*20)
    row_count = 10
    col_count = 10
    player_count = int(input("How many players?\n"))
    players = []
    for i in range(player_count):
        name = input(f"Player {i+1} please enter your name:\n")
        ships = get_ships(name)
        # placement_choice = int(input("How would you like to place your ships?\n"
        #                                 "1-Auto\n"
        #                                 "2-Manual\n"))
        # placement = AutoPlacement(ships, row_count, col_count) if placement_choice == 1 else 1
        human = Human(name, AutoPlacement(ships, row_count, col_count))
        players.append(human)
    if player_count == 1:
        name = 'Computer'
        ships = get_ships(name)
        ai = AI(name, AutoPlacement(ships, row_count, col_count))
        players.append(ai)


    game_type = int(input("What game type do you prefer?\n1-Annihilation\n2-Score\n3-TimeLimit\n"))
    strategy = None
    if game_type == 1:
        strategy = Annihilation()
    elif game_type == 2:
        score = int(input("Please enter the score you would like between(5, 20)\n"))
        strategy = Score(score)
    elif game_type == 3:
        minutes = int(input("Please enter the time limit in minutes.\n"))
        strategy = TimeLimit(minutes)
    else:
        raise ValueError("Unsupported Game Type")

    game = BattleShipGame(players, strategy)

    round = 1
    while not game.has_winner():
        # sleep(1)
        offensive = game.get_next_player()
        # defensive_number = int(input(f"{offensive.name} who would you like to attack?"))
        # defensive = players[defensive_number]
        defensive = random.choice([x for x in game._players if x != offensive])
        avail_cells = defensive.get_unhit_cells()
        i, j = random.choice(avail_cells) # In a real situation a human will make their own choices.
        # (i, j) = [int(x) for x in input(f"{offensive.name} please enter your x y coordinates?").split()]

        hit_report = game.fire(offensive, defensive, (i, j))
        print(f"Round {round}: {offensive.name} played ({i}, {j}): {hit_report}")
        round += 1

    print(f"Congratulations {game.winner.name}, you have own!!! Your final score is {game.winner.score}")