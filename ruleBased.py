from copy import deepcopy as dc
def initializeBoard():
    board={}
    for x in range(1,10):
        board[x]=" "
    return board
def printBoard(board):
        print("-"*13)
        print("|",board[1],"|",board[2],"|",board[3],"|")
        print("-"*13)
        print("|",board[4],"|",board[5],"|",board[6],"|")
        print("-"*13)
        print("|",board[7],"|",board[8],"|",board[9],"|")
        print("-"*13)
def isWin(board,test):
    if (board[1]==test and board[2]==test and board[3]==test) or \
        (board[4]==test and board[5]==test and board[6]==test) or \
        (board[7]==test and board[8]==test and board[9]==test) or \
        (board[1]==test and board[5]==test and board[9]==test) or \
        (board[3]==test and board[5]==test and board[7]==test) or \
        (board[1]==test and board[4]==test and board[7]==test) or \
        (board[2]==test and board[5]==test and board[8]==test) or \
        (board[3]==test and board[6]==test and board[9]==test) :
        return True
    return False
def calculateMove(board):
    #check if we can win
    bestMove=""
    win=False
    for x in range(1,10):
        if board[x]==" ":
            copyBoard=dc(board)
            copyBoard[x]="1"
            if isWin(copyBoard,"1"):
                win=True
                bestMove=x
                return bestMove

    #check if oponent can win
    for x in range(1,10):
        if board[x]==" ":
            copyBoard=dc(board)
            copyBoard[x]="0"
            if isWin(copyBoard,"0"):
                bestMove=x
                return bestMove
    #check if middle is available
    if board[5]==" ":
        bestMove=5
        return bestMove
    #check if empty corner available
    for x in [1,3,7,9]:
        if  board[x]==" ":
            bestMove=x
            return bestMove

    #Else play a remaing space
    for x in [2,4,6,8]:
        if  board[x]==" ":
            bestMove=x
            return bestMove

board=initializeBoard()
printBoard(board)
while True:

    board[calculateMove(board)]="1"
    printBoard(board)
    i=input("Enter your move: ")
    if i=="p":
        break
    i=int(i)
    board[i]="0"
    printBoard(board)
