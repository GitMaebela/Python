import random

board = ["A", "B", "C", "D", "E", "F"]
length = len(board)  

for i in range(length):
    boardPowerBall = random.randrange(1, 21)
    str(boardPowerBall)
    print( board[i],"1(05): # # # # # ",board[i],"2(01):",format(boardPowerBall, '02d'))