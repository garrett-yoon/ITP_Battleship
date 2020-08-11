from AI_opponent import AI_make_a_guess, guess_prev_hit
from boardFunctions import *


# comp_guesses = []

# Testing if adjustment is correct
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=False)
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=True)

# print(comp_guesses)


ships = {"Battleship":4,
             "Submarine":3,
             "Destroyer":3,
             "Patrol Boat":2}
             
# Initialize Game Mode
welcome()
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
<<<<<<< Updated upstream
    board_P2 = comp_placement(board_P2,ships)
    print("-----------------------")

=======
    if mode == 1:
        board_P2 = comp_placement(board_P2,ships)
        print("-----------------------")
        #this initializes the list that the AI will use to keep track of its moves
        previous_guesses = []
        #this is the Boolean that the AI will use to remember if it guessed correctly in its last move
        hit = False
>>>>>>> Stashed changes
    while mode == 1:


        if board_P2=="WIN":
          print("YOU WIN!! Thanks for playing!")
          break
        print_blank_board(board_P2)
        print("-----------------------")
        print_board(board_P1)
        # input("Hit ENTER to end turn.")
        board_P2 = user_move(board_P2)
        board_P1 = comp_move(board_P1)
        print("-----------------------")
        if board_P1=="WIN":
          print("You Lost!! Try again next time!")
          break
        # input("Hit ENTER to end turn.")
    if mode == 2:
        board_P2 = user_placement(board_P2, ships)
    while mode == 2:

        # Player 1's turn. Print blank P2 board and P1 board. 
        print("Player 1 guess:")
        print("\n")
        print("Player 2 board:")
        print_blank_board(board_P2)
        print("-----------------------")
        print("Player 1 board:")
        print_board(board_P1)

        # Player 1's move and check if player 1 wins
        board_P2 = user_move(board_P2)
        if board_P2 =="WIN":
            print("Player 1 Wins!")

        # Player 2's turn
        print("Player 2 guess:")
        print("\n")
        print("Player 1 board:")
        print_blank_board(board_P1)
        print("-----------------------")
        print("Player 2 board:")
        print_board(board_P2)

        # Player 2's move and check if win
        board_P1 = user_move(board_P1)
        if board_P1 =="WIN":
            print("Player 2 Wins!")


elif mode == 3:
    print("Exiting Battleship.")
