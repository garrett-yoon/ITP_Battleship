'''AI_opponent
An AI Player that will play against a human player in Battleship.
This file will contain all of the functions necessary for the AI Player.

----FUNCTIONS----
AI_make_a_guess: will make a guess to target the player's battleship

'''

#import relevant packages
import random

def AI_make_a_guess(board, previous_guesses = [], hit = False):
    '''
    DESCRIPTION: AI will make a guess to target the player's battleships based upon the status of the board, previous guess, and if the previous guess was a hit/miss
    INPUTS (data types):
        board (list of lists) : the grid used to play the game
        previous_guesses (list of lists): a list of the AI's previous guesses, defaults to empty list if the start of a new game
        hit (Boolean): was the previous guess a hit or miss? Default is false
    OUTPUTS (data types):
        next_guess (list with two elements): the AI's next guess. Will give guess in the form of [row, column].
        previous_guesses: an updated list of previous guesses, with the next_guess appended [[row, column], [row, column], ...]
        '''
    #first let's make sure inputs are correct
    #the board should be a list
    assert type(board) == list, 'the board needs to be a list'
    #the columns in board should be a list
    for col in board:
        assert type(board) == list, 'the columns in the board need to be lists'
    #make sure previous_guesses is list
    assert type(previous_guesses) == list, 'previous guesses need to be a list'
    #make sure hit is Boolean
    assert type(hit) == bool, 'hit needs to be a Boolean'

    #let's figure out how big the board is in order to make a guess
    N = len(board)

    #now, we'll handle the situation that either this is the first move of the game or the previous guess was a miss
    if hit == False:

        #now we'll make a random guess based on the board size, guess will be of form [row, column]
        #randint is a uniform distribution, we can change this if we want to get fancy with random distributions (Gaussian, etc.)
        next_guess = [random.randint(0, N - 1), random.randint(0, N - 1)]
        #now we need to make sure that this guess hasn't been guessed before
        if previous_guesses:
            #this we'll keep generating new random guesses as long as we've guessed them before, loop will break with new guess
            while next_guess in previous_guesses:
                next_guess = [random.randint(0, N - 1), random.randint(0, N - 1)]

    #now we'll deal with the situation that the AI's previous guess was right
    if hit == True:
        #extract the guess of the most recent hit
        last_guess = previous_guesses[-1]

        #now generate a new guess based on last guess. The next two lines determine if we're going to move up/down the row and column from the last guess
        row_move = random.randint(-1,1)
        col_move = random.randint(-1,1)

        #make sure that both row and column move are not 0 (i.e., [0,0]). Otherwise we'd make the same guess again!
        while col_move == 0 and row_move == 0:
            row_move = random.randint(-1,1)
            col_move = random.randint(-1,1)

        #now we update our next guess as the sum of the row_move and col_move with our previous guess
        next_guess = [last_guess[0] + row_move, last_guess[1] + col_move]

        #we need to make sure that our next guess doesn't take us off of the board!
        #for the row
        if next_guess[0] < 0:
            next_guess[0] += 1
        if next_guess[0] > N - 1:
            next_guess[0] -= 1

        #for the column
        if next_guess[1] < 0:
            next_guess[1] += 1
        if next_guess[1] > N - 1:
            next_guess[1] -= 1

    #now we add next_guess to our previous previous_guesses
    previous_guesses.append(next_guess)










    return next_guess, previous_guesses
