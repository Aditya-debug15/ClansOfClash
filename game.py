import threading
import time
import os
import sys

from joblib import delayed
import src.variables as vari
from numpy import character
sys.path.append("./src")
import src.board as board

from datetime import datetime
import src.input as inputi

def delayed_attack(board):
    board.king.attack2(board)


now = datetime.now()
dt_string = now.strftime("%d-%m-%Y%H-%M-%S")
file_name = "replay/"+dt_string+".txt"
f = open(file_name, "w")
f.write("==")
f.close()

current_level = 0
print("Select \n 1 for King \n 2 for queen\n")
character_select = input("Enter your choice: ")
os.system('clear')
os.system('clear')
print()
print()
if (current_level == 0):
    board0 = board.Board(character_select,current_level)
    while(True):
        check = inputi.input_to()
        if(check == 'a' or check == 'd' or check == 'w' or check == 's' or check == ' '):
            board0.king.move(board0,check)
        elif(check == 'z'):
            board0.spawning[0].release(board0)
        elif(check == 'x'):
            board0.spawning[1].release(board0)
        elif(check == 'c'):
            board0.spawning[2].release(board0)
        elif(check == 'j'):
            board0.spawning[0].releaseballoon(board0)
        elif(check == 'k'):
            board0.spawning[1].releaseballoon(board0)
        elif(check == 'l'):
            board0.spawning[2].releaseballoon(board0)
        elif(check == 'i'):
            board0.spawning[0].releasearcher(board0)
        elif(check == 'o'):
            board0.spawning[1].releasearcher(board0)
        elif(check == 'p'):
            board0.spawning[2].releasearcher(board0)
        elif(check == 'e' and character_select=='2'):
            t = threading.Timer(1,delayed_attack,[board0])
            t.start()
        elif(check == 'v'):
            for i in board0.enemy:
                i.ragespell()
        elif(check == 'b'):
            for i in board0.enemy:
                i.healspell()
        for i in board0.barbarian:
            i.move(board0)
        for i in board0.balloon:
            i.move(board0)
        for i in board0.cannon:
            i.kill(board0)
        for i in board0.wizard:
            i.kill(board0)
        for i in board0.archer:
            i.move(board0)
        out = board0.render(file_name)
        if(out == 1):
            current_level +=1
            print("\033[%d;%dH" % (2, 2))
            break
        if(out == 2):
            current_level = 4
            break
        if(check=='q'):
            break
if (current_level == 1):
    board1 = board.Board(character_select,current_level)
    while(True):
        check = inputi.input_to()
        if(check == 'a' or check == 'd' or check == 'w' or check == 's' or check == ' '):
            board1.king.move(board1,check)
        elif(check == 'z'):
            board1.spawning[0].release(board1)
        elif(check == 'x'):
            board1.spawning[1].release(board1)
        elif(check == 'c'):
            board1.spawning[2].release(board1)
        elif(check == 'j'):
            board1.spawning[0].releaseballoon(board1)
        elif(check == 'k'):
            board1.spawning[1].releaseballoon(board1)
        elif(check == 'l'):
            board1.spawning[2].releaseballoon(board1)
        elif(check == 'i'):
            board1.spawning[0].releasearcher(board1)
        elif(check == 'o'):
            board1.spawning[1].releasearcher(board1)
        elif(check == 'p'):
            board1.spawning[2].releasearcher(board1)
        elif(check == 'e' and character_select=='2'):
            t = threading.Timer(1,delayed_attack,[board1])
            t.start()
        elif(check == 'v'):
            for i in board1.enemy:
                i.ragespell()
        elif(check == 'b'):
            for i in board1.enemy:
                i.healspell()
        for i in board1.barbarian:
            i.move(board1)
        for i in board1.balloon:
            i.move(board1)
        for i in board1.cannon:
            i.kill(board1)
        for i in board1.wizard:
            i.kill(board1)
        for i in board1.archer:
            i.move(board1)
        out = board1.render(file_name)
        if(out == 1):
            current_level +=1
            print("\033[%d;%dH" % (2, 2))
            break
        if(out == 2):
            current_level = 4
            break
        if(check=='q'):
            break
if (current_level == 2):
    board2 = board.Board(character_select,current_level)
    while(True):
        check = inputi.input_to()
        if(check == 'a' or check == 'd' or check == 'w' or check == 's' or check == ' '):
            board2.king.move(board2,check)
        elif(check == 'z'):
            board2.spawning[0].release(board2)
        elif(check == 'x'):
            board2.spawning[1].release(board2)
        elif(check == 'c'):
            board2.spawning[2].release(board2)
        elif(check == 'j'):
            board2.spawning[0].releaseballoon(board2)
        elif(check == 'k'):
            board2.spawning[1].releaseballoon(board2)
        elif(check == 'l'):
            board2.spawning[2].releaseballoon(board2)
        elif(check == 'i'):
            board2.spawning[0].releasearcher(board2)
        elif(check == 'o'):
            board2.spawning[1].releasearcher(board2)
        elif(check == 'p'):
            board2.spawning[2].releasearcher(board2)
        elif(check == 'e' and character_select=='2'):
            t = threading.Timer(1,delayed_attack,[board2])
            t.start()
        elif(check == 'v'):
            for i in board2.enemy:
                i.ragespell()
        elif(check == 'b'):
            for i in board2.enemy:
                i.healspell()
        for i in board2.barbarian:
            i.move(board2)
        for i in board2.balloon:
            i.move(board2)
        for i in board2.cannon:
            i.kill(board2)
        for i in board2.wizard:
            i.kill(board2)
        for i in board2.archer:
            i.move(board2)
        out = board2.render(file_name)
        if(out == 1):
            current_level +=1
            print("\n !! Victory !! \n")
            break
        if(out == 2):
            current_level = 4
            break
        if(check=='q'):
            break
