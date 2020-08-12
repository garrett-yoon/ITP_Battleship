import copy, random
from time import sleep
from AI_opponent import *

def welcome():
  print("Welcome to Battleship!")
  print("[1] Single Player")
  print("[2] 2-Player")
  print("[3] Exit")

def game_mode():
  while True:
    try:
      mode = int(input("Please select your game mode: "))
    except ValueError:
      print("Please enter a valid option (1, 2, or 3).")
    else:
      print("You selected game mode ", mode)
      print("You can exit the game at any time by typing 'exit'. ")
      if mode not in [1,2,3]:
        print("Not a valid game mode, please try again.")
      break
  return mode

def print_board(board):
    for line in board:
      print(line)

def print_blank_board(board):
  for line in board:
    if isinstance(line, list):
      line = ['-' if i not in ['-', '*', '$'] else i for i in line]
    print(line)


def user_placement(board, ships):
  x, y = '', ''
  for ship in ships.keys():
    valid = False
    while not valid:
      print_board(board)
      print("Placing a " + ship)
      x,y = get_coords()
      orientation = orient()
      if x == "exit" or y == "exit" or orientation == "exit":
          return "exit"
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

  print("Computer's ships stationed successfully.")
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
    if user_input == "v" or user_input == "h" or user_input == "exit":
      return user_input
    else:
      print("Invalid input. Please only enter v or h.")

def get_coords():
    while True:
        user_input = input("Please enter coordinates (row,col) ? ")
        if user_input == "exit":
            return user_input, user_input
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
    if x=="exit" or y=="exit":
        return "exit"
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
        if res == "exit":
            return res

        # Time delay with animation
        s = "FIRING!"
        for i in range(len(s)):
            print(s[i], sep=' ', end=' ', flush=True); sleep(0.5)
        print('\n')
        sleep(0.3)

        if res == "hit":
            print("Success! Hit at " + str(x+1) + "," + str(y+1))
            check_sink(board,x,y)
            board[x][y] = '$'
            if check_win(board):
                return "WIN"
        elif res == "miss":
            print("Sorry, " + str(x+1) + "," + str(y+1) + " is a miss.")
            board[x][y] = "*"
        elif res == "try again":
            print("Sorry, that coordinate was already hit. Please try again")
        sleep(0.5)
        if res != "try again":
            return board

def comp_move(board, previous_guesses = [], hit = False):
    print("-----------------------")
    print("I'm thinking...")
    sleep(1)
    while True:
        #use "smart" AI to make the next guess and keep track of AI's previous guesses
        #this try/except part is just a test to see if hit is being properly passed into function for the AI
        #try:
        #  print('last hit was {}'.format(hit))
        #except:
        #  pass
        #this incorporates the AI into making a guess
        next_guess, previous_guesses = AI_make_a_guess(board, previous_guesses, hit)
        #this is just for testing to see if the AI is using the previous guesses and updating the list
        #print(previous_guesses)
        x, y = next_guess
        res = make_move(board,x,y)
        if res == "hit":
            print("Haha! I hit your ship at " + str(x+1) + "," + str(y+1))
            #to keep track of AI's last move for next round of AI_make_a_guess
            hit = True
            check_sink(board,x,y)
            board[x][y] = '$'
            if check_win(board):
                return "WIN"
            return board, previous_guesses, hit
        elif res == "miss":
            print("Shoot, " + str(x+1) + "," + str(y+1) + " was a miss.")
            board[x][y] = "*"
            #to keep track of AI's last move for next round of AI_make_a_guess
            hit = False
            return board, previous_guesses, hit
        if res != "try again":
            return board, previous_guesses, hit

def check_sink(board,x,y):
  if board[x][y] == "B":
    ship = "Battleship"
  elif board[x][y] == "S":
    ship = "Submarine"
  elif board[x][y] == "D":
    ship = "Destroyer"
  elif board[x][y] == "P":
    ship = "Patrol Boat"
  else:
    return False
  board[-1][ship] -= 1
  if board[-1][ship] == 0:
    print(ship + " sunk")


def check_win(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != "-" and board[i][j] != '*' and board[i][j] != '$':
                return False
    return True
