from click import style
from colorama import Fore, Back, Style
from os import system
import random
from time import sleep, time
import math


class Barbarian():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.health = 1
        self.maxhealth = 1
        self.step = 1
        self.damage = 0.25

    def ragespell(self):
        self.damage *= 2
        self.step *= 2

    def healspell(self):
        newHealth = (3*self.health)/2
        if(newHealth>self.maxhealth):
            newHealth = self.maxhealth
        self.health = newHealth

    def move(self, board):
        if(self.health==0):
            board.barbarian.remove(self)
        else:
            min_dis = 200
            xdestination = 0
            ydestination = 0
            building = ""
            for i in range(board.rows):
                for j in range(board.cols):
                    if(board.board[i][j] == 4 or board.board[i][j] == 5 or board.board[i][j] == 3 or board.board[i][j] == 8):
                        dis = abs(self.xpos-i) + abs(self.ypos-j)
                        if(min_dis > dis):
                            min_dis = dis
                            xdestination = i
                            ydestination = j
                            if(board.board[i][j] == 4):
                                building = 4
                            elif(board.board[i][j] == 3):
                                building = 3
                            elif(board.board[i][j] == 8):
                                building = 8
                            else:
                                building = 5
            if(xdestination != self.xpos):
                # check upar
                if(xdestination < self.xpos):
                    # upar jana hai
                    # just upar kuch object hai
                    if(board.board[self.xpos-1][self.ypos] != 0):
                        if(self.xpos-1 == xdestination and self.ypos == ydestination):
                            if(building == 4):
                                # townhall hai samne
                                board.townhall.health -= self.damage
                            elif(building == 3):
                                temp = [x for x in board.cannon if x.xpos ==
                                    self.xpos-1 and x.ypos == self.ypos]
                                for i in temp:
                                    i.health -= self.damage
                            elif(building == 8):
                                temp = [ x for x in board.wizard if x.xpos ==
                                    self.xpos-1 and x.ypos == self.ypos]
                                for i in temp:
                                    i.health -= self.damage
                            else:
                                temp = [x for x in board.huts if x.xpos ==
                                    self.xpos-1 and x.ypos == self.ypos]
                                for i in temp:
                                    i.health -= self.damage
                        elif(board.board[self.xpos-1][self.ypos] == 2):
                            # upar just wall hai
                            temp = [x for x in board.wall if x.xpos ==
                                self.xpos-1 and x.ypos == self.ypos]
                            for i in temp:
                                i.health -= self.damage
                        elif(board.board[self.xpos-1][self.ypos] != 0):
                            self.ypos += 1
                    # just upar kuch nahi hai to thoda bahut move to karenge
                    else:
                        possible = True
                        for i in range(1, self.step+1):
                            if(self.xpos - i > xdestination):
                                if(board.board[self.xpos - i][self.ypos] != 0):
                                    self.xpos = self.xpos - i + 1
                                    possible = False
                            elif(self.xpos - i >= xdestination):
                                self.xpos = self.xpos - i
                                possible = False
                        if(possible):
                            self.xpos = self.xpos - self.step
                else:
                    if(board.board[self.xpos+1][self.ypos] != 0):
                        if(self.xpos+1 == xdestination and self.ypos == ydestination):
                            if(building == 4):
                                # townhall hai samne
                                board.townhall.health -= self.damage
                            elif(building == 3):
                                temp = [x for x in board.cannon if x.xpos ==
                                    self.xpos+1 and x.ypos == self.ypos]
                                for i in temp:
                                    i.health -= self.damage
                            elif(building == 8):
                                temp = [ x for x in board.wizard if x.xpos ==
                                    self.xpos+1 and x.ypos == self.ypos]
                                for i in temp:
                                    i.health -= self.damage
                            else:
                                temp = [x for x in board.huts if x.xpos ==
                                    self.xpos+1 and x.ypos == self.ypos]
                                for i in temp:
                                    i.health -= self.damage
                        elif(board.board[self.xpos+1][self.ypos] == 2):
                            # neeche just wall hai
                            temp = [x for x in board.wall if x.xpos ==
                                self.xpos+1 and x.ypos == self.ypos]
                            for i in temp:
                                i.health -= self.damage
                        elif(board.board[self.xpos+1][self.ypos] != 0):
                            self.ypos += 1
                    # just neeche kuch nahi hai to thoda bahut move to karenge
                    else:
                        possible = True
                        for j in range(self.step):
                            i = j+1
                            if(self.xpos + i < xdestination):
                                if(board.board[self.xpos + i][self.ypos] == 2):
                                    self.xpos = self.xpos + i - 1
                                    possible = False
                            elif(self.xpos + i <= xdestination):
                                self.xpos = self.xpos + i
                                possible = False
                        if(possible):
                            self.xpos = self.xpos + self.step
            else:
                if(ydestination < self.ypos):
                    # left jana hai
                    # just upar kuch object hai
                    if(board.board[self.xpos][self.ypos-1] != 0):
                        if(self.xpos == xdestination and self.ypos-1 == ydestination):
                            if(building == 4):
                                # townhall hai samne
                                board.townhall.health -= self.damage
                            elif(building == 3):
                                temp = [x for x in board.cannon if x.xpos ==
                                    self.xpos and x.ypos == self.ypos-1]
                                for i in temp:
                                    i.health -= self.damage
                            elif(building == 8):
                                temp = [ x for x in board.wizard if x.xpos ==
                                    self.xpos and x.ypos == self.ypos-1]
                                for i in temp:
                                    i.health -= self.damage
                            else:
                                temp = [x for x in board.huts if x.xpos ==
                                    self.xpos and x.ypos == self.ypos-1]
                                for i in temp:
                                    i.health -= self.damage
                        elif(board.board[self.xpos][self.ypos-1] == 2):
                            # left just wall hai
                            temp = [x for x in board.wall if x.xpos ==
                                self.xpos and x.ypos == self.ypos-1]
                            for i in temp:
                                i.health -= self.damage
                    # just left kuch nahi hai to thoda bahut move to karenge
                    else:
                        possible = True
                        for i in range(1, self.step+1):
                            if(self.ypos - i > ydestination):
                                if(board.board[self.xpos][self.ypos -i] != 0):
                                    self.ypos = self.ypos - i + 1
                                    possible = False
                            elif(self.ypos - i >= ydestination):
                                self.ypos = self.ypos - i + 1
                                possible = False
                        if(possible):
                            self.ypos = self.ypos - self.step  
                              
                else:   
                    if(board.board[self.xpos][self.ypos+1] != 0):
                        if(self.xpos == xdestination and self.ypos+1 == ydestination):
                            if(building == 4):
                                # townhall hai samne
                                board.townhall.health -= self.damage
                            elif(building == 3):
                                temp = [x for x in board.cannon if x.xpos ==
                                    self.xpos and x.ypos == self.ypos+1]
                                for i in temp:
                                    i.health -= self.damage
                            elif(building == 8):
                                temp = [ x for x in board.wizard if x.xpos ==
                                    self.xpos and x.ypos == self.ypos+1]
                                for i in temp:
                                    i.health -= self.damage
                            else:
                                temp = [x for x in board.huts if x.xpos ==
                                    self.xpos and x.ypos == self.ypos+1]
                                for i in temp:
                                    i.health -= self.damage
                        elif(board.board[self.xpos][self.ypos+1] == 2):
                            # left just wall hai
                            temp = [x for x in board.wall if x.xpos ==
                                self.xpos and x.ypos == self.ypos+1]
                            for i in temp:
                                i.health -= self.damage
                    # just right kuch nahi hai to thoda bahut move to karenge
                    else:
                        possible = True
                        for i in range(1, self.step+1):
                            if(self.ypos + i < ydestination):
                                if(board.board[self.xpos][self.ypos +i] != 0):
                                    self.ypos = self.ypos + i - 1
                                    possible = False
                            elif(self.ypos + i <= ydestination):
                                self.ypos = self.ypos + i - 1
                                possible = False
                        if(possible):
                            self.ypos = self.ypos + self.step                                                   

