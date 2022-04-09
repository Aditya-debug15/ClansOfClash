from click import style
from colorama import Fore, Back, Style 
from os import system
import random
from time import sleep,time
import math
from barbarian import Barbarian
from balloon import Balloon
from archer import Archer
class SpawningPoint():
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def release(self,board):
        if(board.maxbar > 0):
            board.maxbar -= 1
            newBarbarian = Barbarian(self.xpos,self.ypos+1)
            board.barbarian.append(newBarbarian)
            board.enemy.append(newBarbarian)
    def releaseballoon(self,board):
        if(board.maxball > 0):
            board.maxball -=1
            newBalloon = Balloon(self.xpos,self.ypos+1)
            board.balloon.append(newBalloon)
            board.enemy.append(newBalloon)
    def releasearcher(self,board):
        if(board.maxarch > 0):
            board.maxarch -= 1
            newArcher = Archer(self.xpos,self.ypos+1)
            board.archer.append(newArcher)
            board.enemy.append(newArcher)