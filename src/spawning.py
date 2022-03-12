from click import style
from colorama import Fore, Back, Style 
from os import system
import random
from time import sleep,time
import math
from barbarian import Barbarian
class SpawningPoint():
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def release(self,board):
        newBarbarian = Barbarian(self.xpos,self.ypos+1)
        board.barbarian.append(newBarbarian)
        board.enemy.append(newBarbarian)