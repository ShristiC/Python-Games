'''
Interactive Tic Tac Toe Game between 2 players:

1 | 2 | 3 
__ ___ ___
4 | 5 | 6
__ ___ ___
7 | 8 | 9
__ ___ ___

'''
import TicTacConstants

# game constants and global variables
game = 0
board = TicTacConstants.table
tracker = TicTacConstants.tracker
posDictionary = TicTacConstants.dic
playerOne = ""
playerTwo = ""
playerDictionary = {}


def printBoard():
    # prints the respective tic tac toe board
    for r in board:
        for c in r:
            print(c, end = " ")
        print()
    print()

def initialSetup():
    global playerOne
    global playerTwo
    # gets player names, intializes player dictionary
    print()
    print(f'TIC TAC TOE GAME {game}')

    # X token
    playerOne = input("Name of first player: ")
    print(f"{playerOne} will be {TicTacConstants.Xtoken}")
    playerDictionary[playerOne] = TicTacConstants.Xtoken

    # Y token
    playerTwo = input('\nName of second player: ')
    print(f"{playerTwo} will be {TicTacConstants.Otoken}")
    playerDictionary[playerTwo] = TicTacConstants.Otoken

    print()


def horizontal(row, token):
    '''
    checks if there is a horizontal tic tac toe match
    param: row position and respective X/O token
    returns true if horizontal match else false
    '''
    counter = 0
    for e in board[row]:
        if e == token:
            counter += 1
    return  counter == 3

def column(col, token):
    '''
    checks if there is a vertical tic tac toe match
    param: col position and respective token
    returns true if there is a column match 
    '''
    counter = 0
    for i in range(3):
        if board[i][col] == token:
            counter += 1
    return counter == 3

def diagonal(token):
    '''
    checks if there is a diagonal match
    param: respective token
    returns true if there is a diagonal match
    '''
    counter = 0 # tracks top left to bottom right
    counter2 = 0 # tracks bottom left to top right
    for i in range(3):
        for j in range(3):
            if i == j and board[i][j] == token:
                counter += 1
                # middle number edge case
                if i == 1:
                    counter2 += 1
            elif i + j == 2 and board[i][j] == token:
                counter2 += 1
    
    return counter == 3 or counter2 == 3

def isWon(row, col, token):
    # early return if horizontal or diagonal match found
    if horizontal(row, token):
        return True
    if column(col, token):
        return True
    # diagonal possibility
    if row == col or row + col == 2:
        return diagonal(token)
    # game not won yet
    return False

def move(person):
    '''
    overarching method that takes user input, places in respective position
    checks for 3 in a row and accordingly returns True/False
    '''
    token = playerDictionary[person]
    # takes user input
    playerPos = input(f'{person} where would you like to place your {token} (#)? ')
    pos = posDictionary[playerPos]
    print()
    # checks that position has not been taken
    if tracker[int(playerPos) - 1] == 0:
        print("unable to place token")
    else:
        board[pos[0]][pos[1]] = token
        tracker[int(playerPos) - 1] = 0
    # prints the new board
    printBoard()
    # checks if a player has won
    return isWon(pos[0], pos[1], token)

def playGame():
    # plays game
    for i in range(8):
        if move(playerOne) == True:
            print(f'Game over! {playerOne} won!')
            break
        if move(playerTwo) == True:
            print(f'Game over! {playerTwo} won!')
            break
    if i == 8:
        print("No one wins, it is a tie!")   

# code structure and game organization
initialSetup()
print(f'This is the initial board')
printBoard()
playGame()