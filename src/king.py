from click import style
from colorama import Fore, Back, Style
from os import system
import random
from time import sleep, time
import math
import input as input


class King():
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.health = 4
        self.maxhealth = 4
        self.step = 1
        self.damage = 1

    def move(self, board,check):
        if(check == 'a'):
            possible = True
            for i in range(1, self.step+1):
                if(self.ypos - i >= 0):
                    if(board.board[self.xpos][self.ypos -i] != 0):
                        self.ypos = self.ypos - i + 1
                        possible = False
                        break
                elif(self.ypos - i < 0):
                    possible = False
            if(possible):
                self.ypos = self.ypos - self.step 
        elif(check == 'd'):
            possible = True
            for i in range(1, self.step+1):
                if(self.ypos + i <= board.cols-1):
                    if(board.board[self.xpos][self.ypos +i] != 0):
                        self.ypos = self.ypos + i - 1
                        possible = False
                        break
                elif(self.ypos + i > board.cols-1):
                    possible = False
            if(possible):
                self.ypos = self.ypos + self.step  
        elif(check == 'w'):
            possible = True
            for i in range(1, self.step+1):
                if(self.xpos - i >= 0):
                    if(board.board[self.xpos - i][self.ypos] != 0):
                        self.xpos = self.xpos - i + 1
                        possible = False
                        break
                elif(self.xpos - i < 0):
                    possible = False
            if(possible):
                self.xpos = self.xpos - self.step
        elif(check == 's'):
            possible = True
            for i in range(1, self.step+1):
                if(self.xpos + i <= board.rows-1):
                    if(board.board[self.xpos + i][self.ypos] != 0):
                        self.xpos = self.xpos + i - 1
                        possible = False
                        break
                elif(self.xpos + i > board.rows-1):
                    possible = False
            if(possible):
                self.xpos = self.xpos + self.step
        elif(check == ' '):
            board.king.attack(board)

    def ragespell(self):
        self.damage *= 2
        self.step *= 2

    def healspell(self):
        newHealth = (3*self.health)/2
        if(newHealth > self.maxhealth):
            newHealth = self.maxhealth
        self.health = newHealth

    def attack(self, board):
        if(self.health>0):
            for j in range(-3,4):
                for i in range(-3,4):
                    if(self.xpos+j >=0 and self.xpos+j <=(board.rows-1) and self.ypos +i >= 0 and self.ypos+i<=(board.cols-1) and (board.board[self.xpos+j][self.ypos+i] == 2 or board.board[self.xpos+j][self.ypos+i] == 5 or board.board[self.xpos+j][self.ypos+i] == 4 or board.board[self.xpos+j][self.ypos+i] == 3 or board.board[self.xpos +j][self.ypos+i] == 8 )):
                        if(board.board[self.xpos+j][self.ypos+i] == 2):
                            temp = [x for x in board.wall if x.xpos ==
                                    self.xpos+j and x.ypos == self.ypos+i]
                            for k in temp:
                                k.health -= self.damage
                        elif(board.board[self.xpos+j][self.ypos+i] == 5):
                            temp = [x for x in board.huts if x.xpos ==
                                    self.xpos+j and x.ypos == self.ypos+i]
                            for k in temp:
                                k.health -= self.damage
                        
                        elif(board.board[self.xpos+j][self.ypos+i] == 4):
                                board.townhall.health -= self.damage
                        elif(board.board[self.xpos+j][self.ypos+i] == 8):
                            temp = [x for x in board.wizard if x.xpos ==
                                    self.xpos+j and x.ypos == self.ypos+i]
                            for k in temp:
                                k.health -= self.damage
                        else:
                            temp = [x for x in board.cannon if x.xpos ==
                                    self.xpos+j and x.ypos == self.ypos+i]
                            for k in temp:
                                k.health -= self.damage

