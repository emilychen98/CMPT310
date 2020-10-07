# AI-TicTacToe

A Tic-Tac-Toe playing program where a human can play against the computer, and the computer makes all its moves using random playouts.
This program does not use any information about Tic-Tac-Toe beyond the essential rules of how to play it, how to determine legal moves, and how to recognize if the game is a win, loss, or draw. 

Random Playout:
* When it’s the computers turn to make a move on a board, a list of all legal moves are compiled.
* For each of the moves, the computer simulates a number of random playouts, playing the game until it is over by making random moves for each player until a win, loss, or draw is reached. 
* The move that results in the minimum number of losses is chosen
