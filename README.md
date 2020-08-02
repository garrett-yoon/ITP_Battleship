# ITP_Battleship
Battleship Project for ITP 2020 Summer NYU

We would like to make a 2-player version of the game Battleship where the user will play against an AI opponent. The player and AI will take turns guessing “shots” to destroy the opposing player’s fleet. The game will be played on a simple 8x8 grid, with (up to?) 4 ships for each player. The ship locations will be generated by player input, while the locations of the AI’s ships will be generated randomly. Ships cannot overlap and may only be laid vertically or horizontally. The player will be notified of whether a player's guess “hits” a ship or not, with the player’s board or tracking grid being updated. When a ship is destroyed, the player will be notified of which ship was destroyed. We also would like to implement weak AI into the program, where if the computer recognizes a hit, it will make subsequent guesses around that area until a ship is sunk. If the AI component becomes too complicated to construct over the 2 weeks that we have to work on the project we will convert to a 2-player human vs. human game. The game will end when one player’s ships have all been eliminated.
Outlined To-Do-List:

1.	Create greeting to the player
2.	Display the types of ships available for player to place as well as the blank board
3.	Have the player place the ships
4.	Display the player’s own board, and display tracking grid (opponent’s board)
5.	Have the player make a guess
6.	Tell the player if guess is a hit or miss
7.	Display the updated boards
8.	Have the AI opponent make a guess, update player on if the AI made a hit or miss
9.	Display the updated boards
10.	Repeat steps 5 - 9 until the game is lost/won
