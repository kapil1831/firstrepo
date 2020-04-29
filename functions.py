import random

def boardcopy(board):
    """  creating Board Copy """
    return [i for i in board]

def board_layout(board):
    """ printing Game Board on the Terminal  """
    print("|"+board[0]+'|'+board[1]+'|'+board[2]+"|")
    print("|"+board[3]+'|'+board[4]+'|'+board[5]+"|")
    print("|"+board[6]+'|'+board[7]+'|'+board[8]+"|")


def isSpaceavailable(board,move):
    """ checking for space available in the GameBoard """
    if board[move-1] == ' ':
        return True
    else:
        return False

def makeMove(board,current_player,move):
    """ Making Move to the Game Board  """
    if isSpaceavailable(board,move):
        board[move-1] = current_player


def isWinner(board,current_player):
    """ finding Winner if any row, columns or digonals by a player  """
    return (board[0]==board[2]==board[1]==current_player or board[4]==board[5]==board[3]==current_player or
        board[7]==board[8]==board[6]==current_player or board[0]==board[3]==board[6]==current_player or
        board[1]==board[4]==board[7]==current_player or board[2]==board[5]==board[8]==current_player or 
        board[2]==board[4]==board[6]==current_player or board[0]==board[4]==board[8]==current_player)

def getRandomMove(board):
    """ helps in making random move on the GameBoard """
    c_pos=[pos for pos in range(1,10) if isSpaceavailable(board,pos) and (pos in [1,3,7,9])]
    if c_pos:
        return random.choice(c_pos)
    o_pos=[pos for pos in range(1,10) if isSpaceavailable(board,pos) and (pos in [2,4,6,8])]
    if o_pos:
        return random.choice(o_pos)


def makePlayerMove(board,player):
    """ inputting from the User Player and returning pos User want to choose  """
    while True:
        try:
            #input
            pos=int(input("Enter your choice from 1-9th : "))
            if not isSpaceavailable(board,pos):
                print("Position is Occupied")
                continue
            else :
                return pos
        except (IndexError, ValueError):
            print("Please Enter position between 1-9")
            continue


def makeComputerMove(board,computer,player):
    """  Computer's  Algorithm to play the Game TicTacToe """
    b_pos=[i for i in range(1,10) if isSpaceavailable(board,i)]
    # part 1
    for move in b_pos:
        cloneBoard=boardcopy(board)
        makeMove(cloneBoard,computer,move)
        if isWinner(cloneBoard,computer):
            return move
    # part 2 
    for move in b_pos:
        cloneBoard=boardcopy(board)
        makeMove(cloneBoard,player,move)
        if isWinner(cloneBoard,player):
            return move

    # part 3
    if isSpaceavailable(board,5):
        return 5
    # part 4
    move = getRandomMove(board)
    return move
    

def WinnerMassage(current_player):
    """  Printing Winner of the Game to current Player """
    print("game ends")
    print("congratulation {} win !!!!!".format(current_player))
    
def GameTied(board):
    """ Declaration is case game is tied """
    c_pos=[pos for pos in range(1,10) if isSpaceavailable(board,pos)]
    if not c_pos:
        board_layout(board)
        print("Game Ends")
        print("Game Tied")
        return True