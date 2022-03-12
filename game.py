import time
import os
import sys
sys.path.append("./src")
import src.board as board
board = board.Board()
count = 0
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y%H-%M-%S")
file_name = "replay/"+dt_string+".txt"
f = open(file_name, "w")
f.write("==")
f.close()

while(True):
    count+=1
    if(count%4==0):
        check = board.king.move(board)
        for i in board.barbarian:
            i.move(board)
        for i in board.cannon:
            i.kill(board)
        if(board.render(file_name)):
            break
        if(check=='q'):
            break