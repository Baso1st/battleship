from abc import ABC, abstractmethod
from random import random
from time import time
from typing import List
from player import Player
import random


class IWinStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_winner(self, players: List[Player]) -> Player:
        pass


class Annihilation(IWinStrategy):
    
    def get_winner(self, players: List[Player]):
        if len(players) == 1:
            return players[0]


class Score(IWinStrategy):
    def __init__(self, score) -> None:
        self._score = score

    def get_winner(self, players: List[Player]):
        if len(players) == 1:
            return players[0]
        for p in players:
            if p._score == self._score:
                return p


class TimeLimit(IWinStrategy):
    def __init__(self, time_limit_in_minutes) -> None:
        self._time_limit = (time_limit_in_minutes * 60)
        self._start_time = time()


    def get_winner(self, players: List[Player]):
        if len(players) == 1:
            return players[0]

        if time() - self._start_time >= self._time_limit:
            max_rank = 0
            winners = []
            for p in players:
                rank = p.score - p.hits
                if rank > max_rank:
                    max_rank == rank
                    winners = [p]
                elif rank == max_rank:
                    winners.append(p)

            # We could have two or more players with the highest score and we should take other things into account to determin the winner,
            # but for simplicity we will just pick a random winner. 
            return random.choice(winners)