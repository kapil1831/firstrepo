import os
from  functions import *

def main_AI():
    want_to_play='y'
    while want_to_play=='y':
        # preparing layout of GameBoard
        board=[]
        for choice in range(0,9):
            board.append(' ')
        board_layout(board)

        #gameplay
        while True:
            #player toogle
            # computer & player Symbol
            player='O'
            computer='X'
            
            # player move
            print("player"+"\'s turn")
            print('player ' +player)
            move=makePlayerMove(board,player)
            makeMove(board,player,move)
            if isWinner(board,player):
                board_layout(board)
                WinnerMassage(player)
                break
            if GameTied(board):
                break
            board_layout(board)
            # computer move
            print("computer"+"\'s turn")
            print('Computer ' + computer)
            move=makeComputerMove(board,computer,player)
            makeMove(board,computer,move)
            os.system("cls")
            if isWinner(board,computer):
                board_layout(board)
                WinnerMassage(computer)
                break
            if GameTied(board):
                break
            board_layout(board)


        want_to_play = input("Do you want to play again (y/n): ")
        os.system('cls')


    print('Exited')
""" UnComment to play"""
# main_AI()
