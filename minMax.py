from copy import deepcopy as dc
from random import randint as ra
def initializeBoard():
    board=list(" "*9)
    return board
def printBoard(board):
        print("-"*13)
        print("|",board[0],"|",board[1],"|",board[2],"|")
        print("-"*13)
        print("|",board[3],"|",board[4],"|",board[5],"|")
        print("-"*13)
        print("|",board[6],"|",board[7],"|",board[8],"|")
        print("-"*13)
def isWin(board,test):
    if (board[0]==test and board[1]==test and board[2]==test) or \
        (board[3]==test and board[4]==test and board[5]==test) or \
        (board[6]==test and board[7]==test and board[8]==test) or \
        (board[0]==test and board[4]==test and board[8]==test) or \
        (board[2]==test and board[4]==test and board[6]==test) or \
        (board[0]==test and board[3]==test and board[6]==test) or \
        (board[1]==test and board[4]==test and board[7]==test) or \
        (board[2]==test and board[5]==test and board[8]==test) :
        return True
    return False
def isDraw(board):
    if board.count(' ') == 0:
        return True
    return False

"""  Min-Max implementation """

def bestMove(board,player):
    if board.count(' ') == 9:
        return 0,4
    if player=='O' :
        opponent = 'X'
    else:
        opponent = 'O'
    if isWin(board,"X") :
        return -1,-1
    elif isWin(board,"O"):
        return 1,-1
    if  board.count(' ') == 0:
        return 0,-1
    results=[]
    for i in range(len(board)):
        if board[i] == ' ':
            tBoard=dc(board)
            tBoard[i]=player
            score,move=bestMove(tBoard,opponent)
            results.append((score,i))
    if player=='O':
        return max(results)
    else :
        return min(results)

"""  Testing """
while True:
    print()
    p=ra(0,1)
    print("Index layout")
    printBoard([1,2,3,4,5,6,7,8,9])
    board=initializeBoard()
    if p==0:
        print("Computer plays first ")
        while not isWin(board,"O") and not isWin(board,"O") and not isDraw(board):
            bestmove=bestMove(board,"O")[1]
            board[bestmove]="O"
            printBoard(board)
            if isWin(board,"O"):
                print("Computer wins")
                break
            i=int(input("Enter your move: "))-1
            board[i]="X"
            printBoard(board)
        else:
            print("Drawn")
    else:
        print("You plays first ")
        while not isWin(board,"O") and not isWin(board,"O") and not isDraw(board):
            i=int(input("Enter your move: "))-1
            board[i]="X"
            printBoard(board)
            bestmove=bestMove(board,"O")[1]
            board[bestmove]="O"
            printBoard(board)
            if isWin(board,"O"):
                print("Computer wins")
                break
        else:
            print("Drawn")
