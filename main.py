# Initialize board

from AI_opponent import AI_make_a_guess, guess_prev_hit
def game_mode():
  while True:
    try:
      mode = int(input("Please select your game mode: "))
    except ValueError:
      print("Please enter a valid option (1, 2, or 3).")
    else:
      print("You selected game mode ", mode)
      break
  return mode


n = 8

board = [['o' for i in range(n)] for i in range(n)]

comp_guesses = []

# Testing if adjustment is correct
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=False)
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=True)
#
# print(comp_guesses)
print("Welcome to Battleship!")
print("[1] Single Player")
print("[2] 2-Player")
print("[3] Exit")
mode = game_mode()

while mode!=3:
  if mode == 1:
    print("game mode {}".format(mode))

    print("Thanks for playing!")
    break
  elif mode == 2:
    print("game mode {}".format(mode))

    print("Thanks for playing!")
    break
  else:
    print("Please try again.")
    mode = game_mode()
