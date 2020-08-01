This is my CS50 final Project.

It is an implementation of the Snakes and Ladders game with some variation in the rules.
It is written entirely in python.
It is played at the python prompt by the two players and the board is graphically represented
and updated using Tkinter and turtle graphics in python.
The rules of the game are:
1. Only two players are allowed.
2. One dies is used for rolling which limits the maximum number of moves to 6.
3. Each roll of the die by a player is automatically updated on the board to show the movement to the new position
4. There are two snakes and two ladders with fixed positions for every game
5. If a player lands on any part of the snake body, the player automatically slides down to the bottom of the snake.
6. If a player lands on any part of the ladder, the player automatically moves up to the top of the ladder.
7. If a player is close to 100, and rolls a number that puts the player above 100, the bounce back variant is used. For
   example, if a player is at 96 and rolls a 6, the bounce back to 98 by moving 4 moves to 100 and 2 moves back to 98
   to complete the 6 moves.
8. A player wins when they roll a number that lands them exactly on 100.
9. Player 1 always goes first
10. After the game ends, clicking anywhere on the game window or on the X button will exit the game.

All the rules have been implemented in python code.
This is CS50.