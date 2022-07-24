
### Make the game extendable/flexable
- Play against the computer
- More than two players
- Different types of boards (square, rectangle, circle, etc...)
- Different winning strategies (Elimination, Time limit, Biggest ships destroyed)
- Need to add a game_config class to pass to the game class. It should contain, row_count, col_count, player_count, etc...

--------------------
- Player one: how would you like to place your ships [Manual, Auto]
- For now we are going to assume a rectanular board and we are sending it to the IShipPlacementStrategy