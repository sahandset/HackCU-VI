import turtle
from random import randint, shuffle
from time import sleep

# Create an empty 9x9 Sodoku board (populated with zeroes)
board = []
for i in range (0, 9):
  board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

# Graphics
myPen = turtle.Turtle()
myPen._tracer()
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()

topLeft_x = -150
topLeft_y = 150

# Writing inside each square
def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)    		  
    myPen.write(message, align = "left", font = FONT)

# Drawing the board 
def draw(board):
  intDim = 35
  for row in range(0, 10):

    if (row % 3) == 0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)

    myPen.penup()
    myPen.goto(topLeft_x, topLeft_y - row * intDim)
    myPen.pendown()
    myPen.goto(topLeft_x + 9 * intDim, topLeft_y - row * intDim)

  for column in range(0, 10):
    if (column % 3) == 0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)    

    myPen.penup()
    myPen.goto(topLeft_x + column * intDim, topLeft_y)
    myPen.pendown()
    myPen.goto(topLeft_x + column * intDim, topLeft_y - 9 * intDim)

  for row in range (0, 9):
      for column in range (0,9):
        if board[row][column] != 0:
          text(board[row][column], topLeft_x + column * intDim + 9, topLeft_y - row * intDim - intDim + 8, 18)

# Checking to see if the board is full. If not, return false, if yes, return true
def check(board):
  for row in range(0, 9):
      for column in range(0, 9):
        if board[row][column] == 0:
          return False
  return True 

# Solve the board using recursive backtracking
def solve(board):
  global counter
  # Iterate through every cell
  for i in range(0, 81):
    row = i // 9
    column = i % 9
    if board[row][column] == 0:
      for value in range (1, 10):
        if not(value in board[row]):
          if not value in (board[0][column],board[1][column],board[2][column],board[3][column],board[4][column],board[5][column],board[6][column],board[7][column],board[8][column]):
            # Working on a specific square
            square = []
            if row < 3:
              if column < 3:
                square = [board[i][0:3] for i in range(0,3)]
              elif column < 6:
                square = [board[i][3:6] for i in range(0,3)]
              else:  
                square = [board[i][6:9] for i in range(0,3)]
            elif row < 6:
              if column < 3:
                square = [board[i][0:3] for i in range(3,6)]
              elif column<6:
                square = [board[i][3:6] for i in range(3,6)]
              else:  
                square = [board[i][6:9] for i in range(3,6)]
            else:
              if column < 3:
                square = [board[i][0:3] for i in range(6,9)]
              elif column < 6:
                square = [board[i][3:6] for i in range(6,9)]
              else:  
                square = [board[i][6:9] for i in range(6,9)]

            #Check that the number has not been used inside the square
            if not value in (square[0] + square[1] + square[2]):
              board[row][column]=value
              if check(board):
                counter += 1
                break
              else:
                if solve(board):
                  return True
      break
  board[row][column] = 0  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 
def fill(board):
  global counter
  # Iterate through every cell
  for i in range(0, 81):
    row = i // 9
    column = i % 9
    if board[row][column] == 0:
      shuffle(numbers)      
      for value in numbers:
        if not(value in board[row]):
          if not value in (board[0][column],board[1][column],board[2][column],board[3][column],board[4][column],board[5][column],board[6][column],board[7][column],board[8][column]):
            # Working on a specific square
            square = []
            if row < 3:
              if column < 3:
                square = [board[i][0:3] for i in range(0,3)]
              elif column < 6:
                square = [board[i][3:6] for i in range(0,3)]
              else:  
                square = [board[i][6:9] for i in range(0,3)]
            elif row < 6:
              if column < 3:
                square = [board[i][0:3] for i in range(3,6)]
              elif column < 6:
                square = [board[i][3:6] for i in range(3,6)]
              else:  
                square = [board[i][6:9] for i in range(3,6)]
            else:
              if column < 3:
                square = [board[i][0:3] for i in range(6,9)]
              elif column<6:
                square = [board[i][3:6] for i in range(6,9)]
              else:  
                square = [board[i][6:9] for i in range(6,9)]

            #Check that this number has not already been used in this square
            if not value in (square[0] + square[1] + square[2]):
              board[row][column]=value
              if check(board):
                return True
              else:
                if fill(board):
                  return True
      break
  board[row][column] = 0             
    
fill(board)
draw(board) 
myPen.getscreen().update()
sleep(1)

numAttempts = 5 
counter = 1
while numAttempts > 0:
  # Select a random cell that is not emptys
  row = randint(0, 8)
  column = randint(0, 8)
  while board[row][column] == 0:
    row = randint(0, 8)
    column = randint(0, 8)
  # Remember cell value
  backup = board[row][column]
  board[row][column] = 0
  
  # Make a copy of the board
  copy = []
  for i in range(0, 9):
     copy.append([])
     for j in range(0,9):
        copy[i].append(board[i][j])
  
  counter = 0      
  solve(copy)   

  if counter != 1:
    board[row][column] = backup

    numAttempts -= 1
  
  myPen.clear()
  draw(board) 
  myPen.getscreen().update()

print("The Board is ready!")
turtle.done()