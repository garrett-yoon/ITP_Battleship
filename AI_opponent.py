'''AI_opponent
An AI Player that will play against a human player in Battleship.
This file will contain all of the functions necessary for the AI Player.

----FUNCTIONS----
AI_make_a_guess: will make a guess to target the player's battleship
guess_prev_hit: a support function for AI_make_a_guess in the case that the AI guessed correctly last time
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
        next_guess = [random.randint(0, N - 2), random.randint(0, N - 2)]
        #now we need to make sure that this guess hasn't been guessed before
        if previous_guesses:
            #this we'll keep generating new random guesses as long as we've guessed them before, loop will break with new guess
            while next_guess in previous_guesses:
                next_guess = [random.randint(0, N - 2), random.randint(0, N - 2)]

    #now we'll deal with the situation that the AI's previous guess was right
    if hit == True:
        #extract the guess of the most recent hit
        last_guess = previous_guesses[-1]

        #call function for previous hit
        next_guess = guess_prev_hit(board, previous_guesses, last_guess)

        #make sure that it's not a previous guess
        #this we'll keep generating new random guesses as long as we've guessed them before, loop will break with new guess
        while next_guess in previous_guesses:
            next_guess = guess_prev_hit(board, previous_guesses, last_guess)

    #now we add next_guess to our previous previous_guesses
    previous_guesses.append(next_guess)

    #return the next guess and list of previous guesses
    return next_guess, previous_guesses

def guess_prev_hit(board, previous_guesses, last_guess):
    '''
    DESCRIPTION: a function to support AI_make_a_guess in the situation that the AI's last guess was a hit
    INPUTS (data types):
        board (list of lists) : the grid used to play the game
        previous_guesses (list of lists): a list of the AI's previous guesses, defaults to empty list if the start of a new game
        last_guess (list with two elements): the AI's last guess, of the form [row, column]
    OUTPUTS (data types):
        next_guess (list with two elements): the AI's next guess. Will give guess in the form of [row, column].
    '''
    # Get length of board
    N = len(board)

    # List of all adjacent positions
    combos = ([0,1], [1,0], [-1,0], [0,-1])

    #
    validGuess = False

    while validGuess == False:

        #randomly generate a column/row movement
        movement = combos[random.randint(0,3)]

        #now we update our next guess
        next_guess = [last_guess[0] + movement[0], last_guess[1] + movement[1]]

        #checks if guess is valid (within the range of 0 to N-1)
        if next_guess[0] >= 0 and next_guess[1] <= N - 2:
            validGuess = True

    # return the next guess
    return next_guess
