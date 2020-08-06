# Initialize board

from AI_opponent import AI_make_a_guess, guess_prev_hit

n = 8

board = [['o' for i in range(n)] for i in range(n)]

comp_guesses = []

# Testing if adjustment is correct
cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=False)
cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=True)

print(comp_guesses)


