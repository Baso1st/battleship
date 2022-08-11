import unittest

from gameloop import *



class TestBattleShip(unittest.TestCase):
    def test_two_players_auto_placement_annihilation(self):
        players = []
        for i in [1, 2]:
            name = f'TestPlayer {i}'
            ships = get_ships(name)
            placement_strategy = AutoPlacement(ships, 10, 10)
            players.append(Human(name, placement_strategy))

        game = BattleShipGame(players, Annihilation())

        round = 1
        while not game.has_winner():
            offensive = game.get_next_player()
            defensive = random.choice([x for x in game._players if x != offensive])
            avail_cells = defensive.get_unhit_cells()
            i, j = random.choice(avail_cells)
            hit_report = game.fire(offensive, defensive, (i, j))
            round += 1

        self.assertIn(game.winner.name, ['TestPlayer 1', 'TestPlayer 2'], "Unnknown winner!!!")
        self.assertLessEqual(round, 200, 'Rounds exceeded rows * cols * 2!!!')
    

if __name__ == '__main__':
    unittest.main()
