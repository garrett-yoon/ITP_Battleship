from AI_opponent import AI_make_a_guess, guess_prev_hit
from boardFunctions import *



ships = {"Battleship":4,
             "Submarine":3,
             "Destroyer":3,
             "Patrol Boat":2}



# comp_guesses = []

# Testing if adjustment is correct
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=False)
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=True)

# print(comp_guesses)

print("Welcome to Battleship!")
print("[1] Single Player")
print("[2] 2-Player")
print("[3] Exit")

# Initialize Game Mode
mode = ''
while mode not in [1,2,3]:
    mode = game_mode()

#setup blank 8x8 board
board = []
n = 8
for i in range(n):
    board_row = []
    for j in range(n):
        board_row.append("-")
    board.append(board_row)

board_P1 = copy.deepcopy(board)
board_P2 = copy.deepcopy(board)
board_P1.append(copy.deepcopy(ships))
board_P2.append(copy.deepcopy(ships))

if mode in [1,2]:

    #ship placement
    board_P1 = user_placement(board_P1,ships)
    board_P2 = comp_placement(board_P2,ships)
    print("-----------------------")

    while mode == 1:
        board_P2 = user_move(board_P2)
        print("-----------------------")
        if board_P2=="WIN":
          print("YOU WIN!! Thanks for playing!")
          break
        print_board(board_P2)
        print("-----------------------")
        print_board(board_P1)
        input("Hit ENTER to end turn.")
        board_P1 = comp_move(board_P1)
        print("-----------------------")
        if board_P1=="WIN":
          print("You Lost!! Try again next time!")
          break
        input("Hit ENTER to end turn.")

    while mode == 2:
        print("game mode {}".format(mode))


elif mode == 3:
    print("Exiting Battleship.")
