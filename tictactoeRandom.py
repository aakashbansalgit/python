import random
import sys
board = ["-"] * 9

def displayboard():
  print (board[0] + '|' + board[1] + '|' + board[2])
  print (board[3] + '|' + board[4] + '|' + board[5])
  print (board[6] + '|' + board[7] + '|' + board[8])

def playgame():
  displayboard()
  k = int(input ("0 for Two Player Mode, 1 for Single Player Mode and 2 for Closing the Game:"))
  if k == 0:
    handleturn2player()
  elif k == 1:
    handleturn1player()
  elif k == 2:
    sys.exit()
  else:
    print("invalid input!")
    playgame()

def handleturn1player():
  print ("Your Turn")
  entercrossmark()
  if checkboard():
    print ("Game Drawn!")
    resetboard()
  else:
    computerturn()

def handleturn2player():
  print ("Player 1's turn")
  entercrossmark()
  if checkboard():
    print ("Game Drawn!")
    resetboard()
  else:
    print ("Player 2's turn")
    enterticmark()

def checkwinplayer1():
  if ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X')):
    return True
  elif ((board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X')):
    return True
  elif ((board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
    return True
  else:
    return False

def checkwinplayer2():
  if ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O')):
    return True
  elif ((board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O')):
    return True
  elif ((board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
    return True
  else:
    return False

def checkwincomputer():
  if ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O')):
    return True
  elif ((board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O')):
    return True
  elif ((board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
    return True
  else:
    return False

def checkfilled():
  for i in range (9):
    if (board[i] == '-'):
      return False

def entercrossmark():
  position = input("Choose from 1-9:")
  position = int(position) - 1
  if position in range(9):
    if board[position] == '-':
      board[position] = 'X'
      displayboard()
      if checkwinplayer1():
        print ("Player 1 VICTORY!")
        resetboard()
      elif checkfilled():
        print ("This game is a DRAW!")
        resetboard()
    else:
      print('invalid input!')
      entercrossmark()
  else:
    print('invalid input!')
    entercrossmark()

def enterticmark():
  position = input("Choose from 1-9:")
  position = int(position) - 1
  if position in range(9):
    if board[position] == '-':
      board[position] = 'O'
      displayboard()
      if checkwinplayer2():
        print ("Player 2 VICTORY!")
        resetboard()
      else:
        handleturn2player()
    else:
      print('invalid input!')
      enterticmark()
  else:
    print('invalid input!')
    enterticmark()

def computerturn():
  arr = checkempty()
  position = random.choice(arr)
  if board[position] == '-':
    board[position] = 'O'
    print("Computer's Turn:")
    displayboard()
    if checkwincomputer():
      print ("You Lost!")
      resetboard()
    else:
      handleturn1player()
  else:
    print('invalid input!')
    enterticmark()

def resetboard():
  for i in range (9):
    board[i] = '-'
  playgame()

def checkboard():
  arr = checkempty()
  if arr == []:
    return True

def checkempty():
  arr = []
  for i in range (9):
    if board[i] == '-':
      arr.append(i)
  return arr

playgame()
















# display - board
# alternating turns
# computer response
# check win
  # check row
  # check comlumn
  # check diagonal
# check draw