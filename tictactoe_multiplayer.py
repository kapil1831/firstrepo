import os
from functions import *

def multiplayer():
    want_to_play='y'
    while want_to_play=='y':
        # layout
        board=[]
        for choice in range(0,9):
            board.append(' ')
        board_layout(board)
        #gameplay
        player=False
        while True:
            #player toogle
            if not player :
                print("player"+str(player + 1)+"\'s turn")
                symbol='X'
                print('player ' + symbol)
                current_player="player"+str(player + 1)
            else:
                print("player"+str(player + 1)+"\'s turn")
                symbol='O'
                print('player ' + symbol)
                current_player="player"+str(player + 1)
            #Exception Handeling
            move=makePlayerMove(board,player)
            makeMove(board,symbol,move)
            os.system("cls")
            board_layout(board)
            if isWinner(board,symbol):
                WinnerMassage(current_player)
                break
            if GameTied(board):
                    break

            player = not player
        want_to_play = input("Do you want to play again (y/n): ")
        os.system('cls')
    print('Exited')

""" UnComment to play"""
# multiplayer() 

























    
