from pickle import TRUE
from click import style
from colorama import Fore, Back, Style
from os import system
import random
from time import sleep, time
import math

class Buildings():
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos   

class WizardTower():
    def __init__(self,xpos,ypos,energy):
        self.xpos = xpos
        self.ypos = ypos
        self.energy = energy
        self.damage = 0.5
        self.shoot = False
        self.health = 2
    
    def kill(self, board):
        if(self.health<=0):
            board.wizard.remove(self)
            return

        self.shoot = False
        xcordinate = 0
        ycordinate = 0
        enemy = 0
        min_dis = 100
        for i in range(-5, 6):
            for j in range(-5, 6):
                if(i+self.xpos < board.rows and i+self.xpos >= 0 and j+self.ypos < board.cols and j+self.ypos >= 0 and (board.board[i+self.xpos][j+self.ypos] == 1 or board.board[i+self.xpos][j+self.ypos] == 7 or board.board[i+self.xpos][j+self.ypos] == 9 or board.board[i+self.xpos][j+self.ypos] == 10)):
                    dis = i + j
                    if(dis < min_dis):
                        min_dis = dis
                        xcordinate = i+self.xpos
                        ycordinate = j+self.ypos
                        enemy = board.board[i+self.xpos][j+self.ypos]
        if(enemy !=0):
            self.shoot = True
            for i in range(-1,2):
                for j in range(-1,2):
                    if(i+xcordinate < board.rows and i+xcordinate >= 0 and j+ycordinate < board.cols and j+ycordinate >= 0):
                        if(board.board[i+xcordinate][j+ycordinate] == 1):
                            if(board.king.health>0):
                                if(board.king.health > self.damage):
                                    board.king.health -= self.damage
                                else:
                                    board.king.health = 0
                        elif(board.board[i+xcordinate][j+ycordinate] == 7):
                            temp = [x for x in board.barbarian if x.xpos == i+xcordinate and x.ypos == j+ycordinate]
                            for z in temp:
                                z.health -= self.damage
                        elif(board.board[i+xcordinate][j+ycordinate] == 9):
                            temp = [x for x in board.archer if x.xpos == i+xcordinate and x.ypos == j+ycordinate]
                            for z in temp:
                                z.health -= self.damage
                        elif(board.board[i+xcordinate][j+ycordinate] == 10):
                            temp = [x for x in board.balloon if x.xpos == i+xcordinate and x.ypos == j+ycordinate]
                            for z in temp:
                                z.health -= self.damage

                            

class Cannon():
    def __init__(self, xpos, ypos, energy):
        self.xpos = xpos
        self.ypos = ypos
        self.energy = energy
        self.damage = 0.5
        self.shoot = False
        self.health = 2

    def kill(self, board):
        if(self.health<=0):
            board.cannon.remove(self)
            return
        self.shoot = False
        self.energy = 0
        xcordinate = 0
        ycordinate = 0
        enemy = 0
        min_dis = 100
        for i in range(-5, 6):
            for j in range(-5, 6):
                if(i+self.xpos < board.rows and i+self.xpos >= 0 and j+self.ypos < board.cols and j+self.ypos >= 0 and (board.board[i+self.xpos][j+self.ypos] == 1 or board.board[i+self.xpos][j+self.ypos] == 7)):
                    dis = i + j
                    if(dis < min_dis):
                        min_dis = dis
                        xcordinate = i+self.xpos
                        ycordinate = j+self.ypos
                        enemy = board.board[i+self.xpos][j+self.ypos]
        if(enemy!=0):
            self.shoot = True
            if(enemy == 1):
                if(board.king.health>0):
                    if(board.king.health > self.damage):
                        board.king.health -= self.damage
                    else:
                        board.king.health = 0
            elif(enemy == 7):
                temp = [x for x in board.barbarian if x.xpos == xcordinate and x.ypos == ycordinate]
                for i in temp:
                    i.health -= self.damage
            elif(enemy == 9):
                temp = [x for x in board.archer if x.xpos == i+xcordinate and x.ypos == j+ycordinate]
                for z in temp:
                    z.health -= self.damage                   
                # shoot kara denge




class Hut(Buildings):
    def __init__(self,xpos,ypos):
        Buildings.__init__(self,xpos,ypos)
        self.health = 5

class TownHall(Buildings):
    def __init__(self,xpos,ypos):
        Buildings.__init__(self,xpos,ypos)
        self.health = 10

class Wall():
    def __init__(self,x,y):
        self.xpos = x
        self.ypos = y
        self.health = 1