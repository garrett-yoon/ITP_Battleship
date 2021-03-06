from AI_opponent import AI_make_a_guess, guess_prev_hit
from boardFunctions import *

# Create ships dictionary
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

# Create player boards
board_P1 = copy.deepcopy(board)
board_P2 = copy.deepcopy(board)
board_P1.append(copy.deepcopy(ships))
board_P2.append(copy.deepcopy(ships))

# Check game mode
if mode in [1,2]:

    #ship placement
    board_P1 = user_placement(board_P1,ships)

    # board_P2 = comp_placement(board_P2,ships)
    print("-----------------------")
    if board_P1 == "exit":
        mode = 3
        print("Exiting Battleship.")

    if mode == 1:
        board_P2 = comp_placement(board_P2,ships)
        print("-----------------------")
        #this initializes the list that the AI will use to keep track of its moves
        previous_guesses = []
        #this is the Boolean that the AI will use to remember if it guessed correctly in its last move
        hit = False

    # Loop for single player game
    while mode == 1:

        if board_P2=="WIN":
          print("YOU WIN!! Thanks for playing!")
          break
        print_blank_board(board_P2)
        print("-----------------------")
        print_board(board_P1)
        # input("Hit ENTER to end turn.")
        board_P2 = user_move(board_P2)
        if board_P2 == "exit":
            print("Exiting Battleship.")
            break
        
        #incorporating previous_guesses and hit into the AI's moves so that it uses its memory from the previous move
        board_P1, previous_guesses, hit = comp_move(board_P1, previous_guesses , hit)
        print("-----------------------")
        if board_P1=="WIN":
          print("You Lost!! Try again next time!")
          break
        # input("Hit ENTER to end turn.")

    # Create 2nd player's board if mode 2 selected
    if mode == 2:
        print("-----------------------")
        print("-----------------------")
        print("Player 2 ship placement:")
        board_P2 = user_placement(board_P2, ships)

    # Loop for 2 player game
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
        if board_P2 == "exit":
            print("Exiting Battleship.")
            break
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
        if board_P1 == "exit":
            print("Exiting Battleship.")
            break
        if board_P1 =="WIN":
            print("Player 2 Wins!")

elif mode == 3:
    print("Exiting Battleship.")
