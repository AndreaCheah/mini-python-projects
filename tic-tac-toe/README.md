# Breakdown of the Game

### 1. Board Representation
The board is represented as a list of 9 spaces, where each space can be an 'X', 'O', or ' '.

### 2. Game State
The state of the game includes:  
a) the board (each position contains which symbol)  
b) who is the current player making a move  
c) whether game is over (when there is a win or tie)

### 3. Player and Computer Moves
Alternate turns between player and computer.

### 4. Game Over Condition
A function that checks all rows, columns, and diagonals for a winner, or if all spaces are filled for a tie.

### 5. Human Input
Ensure that the move is valid:  
a) within board range  
b) on an empty space.

### 6. Computer AI
For now, the computer player is a basic player and randomly selects an empty spot.

### 7. Rough Outline of the Program Logic
```
while not game_over:  
    display_board()  
    get_current_player_move()
    update_board()
    check_for_winner_or_tie()
    switch_player()
```
