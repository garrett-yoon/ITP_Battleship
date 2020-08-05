'''AI_opponent
An AI Player that will play against a human player in Battleship.
This file will contain all of the functions necessary for the AI Player.

----FUNCTIONS----
AI_make_a_guess: will make a guess to target the player's battleship

'''

#import relevant packages
import

def AI_make_a_guess(board, previous_guesses = [], hit = False):
    '''
    DESCRIPTION: AI will make a guess to target the player's battleships based upon the status of the board, previous guess, and if the previous guess was a hit/miss
    INPUTS (data types):
        board (list of lists) : the grid used to play the game
        previous_guesses (list of lists): a list of the AI's previous guesses, defaults to empty list if the start of a new game
        hit (Boolean): was the previous guess a hit or miss? Default is false
    OUTPUTS (data types):
        next_guess (list with two elements): the AI's next guess. Will give guess in the form of [row, column].
        previous_guesses: an updated list of previous guesses, with the next_guess appended
        '''
    #first let's make sure inputs are correct
    #the board should be a list
    assert type(board) == list, 'the board needs to be a list'
    #the columns in board should be a list
    for col in board:
        assert type(board) == list, 'the columns in the board need to be lists'
    #make sure previous_guesss is list
    assert type(previous_guesses) == list, 'previous guesses need to be a list'
    #make sure hit is Boolean
    assert type(hit) == bool, 'hit needs to be a Boolean'

    #first, we'll handle the situation that either this is the first move of the game or the previous guess was a miss
    if hit == False:
        



    return next_guess, previous_guesses
