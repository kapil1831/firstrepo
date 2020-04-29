import os
import random
from functions import *





print("\t\t\t Welcome To TicTacToe ")
print("\t\t\t----------------------")

print("""
Press 1: Player vs Computer
Press 2: MultiPlayer(Player1 vs Player2) 
Press 3: Exit Game
""")


while True:
    try:
        choice=int(input("Enter Your Choice : "))
        break
    except (IndexError, ValueError):
        print("Please Enter Valid Choice")

if choice == 1:
    from tictactoe_AI import main_AI
    main_AI()

elif choice == 2:
    from tictactoe_multiplayer import multiplayer
    multiplayer()

elif choice == 3:
    exit()

