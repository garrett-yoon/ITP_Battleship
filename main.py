# Initialize board

from AI_opponent import AI_make_a_guess, guess_prev_hit
import copy, random
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

def print_board(board):
    for line in board:
      print(line)

def user_placement(board, ships):
  for ship in ships.keys():
    valid = False
    while not valid:
      print_board(board)
      print("Placing a " + ship)
      x,y = get_coords()
      orientation = orient()
      valid = validate(board,ships[ship],x,y,orientation)
      if not valid:
        print("Invalid ship placement. Please try again.")
        input("Press ENTER to continue")
    board = place_ship(board,ships[ship],ship[0],x,y,orientation)
    print_board(board)
  print("Ships stationed successfully.")
  return board

def comp_placement(board, ships):
  for ship in ships.keys():
    valid = False
    while not valid:
      x = random.randint(1,8)-1
      y = random.randint(1,8)-1
      temp = random.randint(0,1)
      if temp==0:
        orientation = "v"
      else:
        orientation = "h"
      valid = validate(board,ships[ship],x,y,orientation)
    board = place_ship(board,ships[ship],ship[0],x,y,orientation)
  print("Ships stationed successfully.")
  return board

def place_ship(board, ship, c, x, y, orientation):
  if orientation == "v":
    for i in range(ship):
      board[x+i][y]=c
  elif orientation == "h":
    for i in range(ship):
      board[x][y+i]=c
  return board

def validate(board, ship, x, y, orientation):
  if orientation == "v" and x+ship>8:
    return False
  elif orientation == "h" and y+ship >8:
    return False
  else:
    if orientation == "v":
      for i in range(ship):
        if board[x+i][y] != '-':
          return False
    elif orientation == "h":
      for i in range(ship):
        if board[x][y+i] != '-':
          return False
  return True

def orient():
  while True:
    user_input = input("vertical or horizontal (v,h) ? ")
    if user_input == "v" or user_input == "h":
      return user_input
    else:
      print("Invalid input. Please only enter v or h.")

def get_coords():
	while True:
		user_input = input("Please enter coordinates (row,col) ? ")
		try:
			coords = user_input.split(",")
			if len(coords) != 2:
				raise Exception("Invalid entry, too few/many coordinates.");
			coords[0] = int(coords[0])-1
			coords[1] = int(coords[1])-1
			if coords[0] > 7 or coords[0] < 0 or coords[1] > 7 or coords[1] < 0:
				raise Exception("Invalid entry. Please use values between 1 to 8 only.")
			return coords
		except ValueError:
			print("Invalid entry. Please enter only numeric values for coordinates")
		except Exception as e:
			print(e)

def make_move(board,x,y):
	if board[x][y] == '-':
		return "miss"
	elif board[x][y] == '*' or board[x][y] == '$':
		return "try again"
	else:
		return "hit"

def user_move(board):
	while True:
		x,y = get_coords()
		res = make_move(board,x,y)
		if res == "hit":
			print("Hit at " + str(x+1) + "," + str(y+1))
			check_sink(board,x,y)
			board[x][y] = '$'
			if check_win(board):
				return "WIN"
		elif res == "miss":
			print("Sorry, " + str(x+1) + "," + str(y+1) + " is a miss.")
			board[x][y] = "*"
		elif res == "try again":
			print("Sorry, that coordinate was already hit. Please try again")
		if res != "try again":
			return board

def comp_move(board):
	while True:
		x = random.randint(1,8)-1
		y = random.randint(1,8)-1
		res = make_move(board,x,y)
		if res == "hit":
			print("Hit at " + str(x+1) + "," + str(y+1))
			check_sink(board,x,y)
			board[x][y] = '$'
			if check_win(board):
				return "WIN"
		elif res == "miss":
			print("Sorry, " + str(x+1) + "," + str(y+1) + " is a miss.")
			board[x][y] = "*"
		if res != "try again":
			return board

def check_sink(board,x,y):
	if board[x][y] == "B":
		ship = "Battleship"
	elif board[x][y] == "S":
		ship = "Submarine"
	elif board[x][y] == "D":
		ship = "Destroyer"
	elif board[x][y] == "P":
		ship = "Patrol Boat"

	board[-1][ship] -= 1
	if board[-1][ship] == 0:
		print(ship + " sunk")


def check_win(board):
	for i in range(8):
		for j in range(8):
			if board[i][j] != "-" and board[i][j] != '*' and board[i][j] != '$':
				return False
	return True


# def single_player():
#   for line in board_P1:
#     print(line)


n = 8

# board_P1 = [['o' for i in range(n)] for i in range(n)]
# board_P2 = [['o' for i in range(n)] for i in range(n)]
ships = {"Battleship":4,
 		     "Submarine":3,
		     "Destroyer":3,
		     "Patrol Boat":2}

	#setup blank 8x8 board

# comp_guesses = []

# Testing if adjustment is correct
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=False)
# cur_guess, comp_guesses = AI_make_a_guess(board, comp_guesses, hit=True)

# print(comp_guesses)

print("Welcome to Battleship!")
print("[1] Single Player")
print("[2] 2-Player")
print("[3] Exit")
mode = game_mode()

board = []
for i in range(n):
	board_row = []
	for j in range(n):
		board_row.append("-")
	board.append(board_row)

board_P1 = copy.deepcopy(board)
board_P2 = copy.deepcopy(board)
board_P1.append(copy.deepcopy(ships))
board_P2.append(copy.deepcopy(ships))

#ship placement
board_P1 = user_placement(board_P1,ships)
board_P2 = comp_placement(board_P2,ships)

while mode!=3:
  if mode == 1:
    board_P2 = user_move(board_P2)
    if board_P2=="WIN":
      print("YOU WIN!! Thanks for playing!")
      break
    print_board(board_P2)
    print("-----------------------")
    print_board(board_P1)
    input("Hit ENTER to end turn.")
    board_P1 = comp_move(board_P1)
    if board_P1=="WIN":
      print("You Lost!! Try again next time!")
      break
    input("Hit ENTER to end turn.")
  elif mode == 2:
    print("game mode {}".format(mode))

    print("Thanks for playing!")
    break
  else:
    print("Please try again.")
    mode = game_mode()
