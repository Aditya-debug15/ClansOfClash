
import imp
import black
from click import style
from colorama import Fore, Back, Style
from os import system
import random
from time import sleep, time
import math
from numpy import var

from zmq import BACKLOG
from king import King
from building import Hut, TownHall, Cannon, Wall
from random import randint
import variables as variables
from spawning import SpawningPoint
from barbarian import Barbarian
printing_purpose = {0: Back.GREEN+' '+Style.RESET_ALL,
                    1: Back.RED + 'K' + Style.RESET_ALL,
                    2: Back.BLACK + 'W' + Style.RESET_ALL,
                    3: {0: Back.LIGHTRED_EX + Fore.LIGHTMAGENTA_EX + 'C' + Style.RESET_ALL, 1: Back.LIGHTYELLOW_EX + Fore.LIGHTMAGENTA_EX + 'C' + Style.BRIGHT + Style.RESET_ALL},
                    4: {0: Back.BLUE + Fore.LIGHTMAGENTA_EX + 'T' + Style.RESET_ALL, 1: Back.YELLOW + Fore.LIGHTMAGENTA_EX + 'T' + Style.RESET_ALL, 2: Back.MAGENTA + Fore.LIGHTGREEN_EX + 'T' + Style.RESET_ALL},
                    5: {0: Back.BLUE + Fore.LIGHTMAGENTA_EX + 'H' + Style.RESET_ALL, 1: Back.YELLOW + Fore.LIGHTMAGENTA_EX + 'H' + Style.RESET_ALL, 2: Back.MAGENTA + Fore.LIGHTGREEN_EX + 'H' + Style.RESET_ALL},
                    6: '\x1b[5;30;43m' + 'S' + '\033[0m',
                    7: {0: Back.WHITE + Fore.BLACK + 'B' + Style.RESET_ALL, 1: Back.LIGHTYELLOW_EX + Fore.BLACK + 'B' + Style.RESET_ALL}
}
'''

0  -- grass
1  -- king
2  -- Wall
3  -- Cannon
4  -- TownHall
5  -- Hut
6  -- Spawning Point
7  -- Barbarian
'''


class Board():
    def __init__(self):
        self.cols = 75
        self.rows = 30
        self.game_over = False
        self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
        self.king = King()
        self.wall = []
        self.game_over = False
        i = variables.WALLX[0]
        for j in range(variables.WALLY[0], variables.WALLY[1]):
            self.wall.append(Wall(i, j))
        i = variables.WALLX[1]
        for j in range(variables.WALLY[0], variables.WALLY[1]):
            self.wall.append(Wall(i, j))
        j = variables.WALLY[0]
        for i in range(variables.WALLX[0], variables.WALLX[1]):
            self.wall.append(Wall(i, j))
        j = variables.WALLY[1] - 1
        for i in range(variables.WALLX[0], variables.WALLX[1]):
            self.wall.append(Wall(i, j))

        self.huts = []
        for i in variables.HUTS:
            TempHut = Hut(i[0], i[1])
            self.huts.append(TempHut)
        self.townhall = TownHall(variables.TOWNHALL[0], variables.TOWNHALL[1])
        self.cannon = [Cannon(variables.CANNON[0][0], variables.CANNON[0][1], randint(0, 40)), Cannon(
            variables.CANNON[1][0], variables.CANNON[1][1], randint(0, 40))]
        self.spawning = []
        for i in variables.SPAWNINGPOINT:
            TempSpawning = SpawningPoint(i[0], i[1])
            self.spawning.append(TempSpawning)
        self.board = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.barbarian = []
        self.enemy = []
        self.enemy.append(self.king)

    def render(self, file_name):
        self.board = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.printBoard = [[self.bg_pixel for j in range(
            self.cols)] for i in range(self.rows)]
        self.RenderWalls()
        self.RenderHuts()
        self.RenderCannon()
        self.RenderTownHall()
        self.RenderSpawning()
        self.RenderBarbarian()
        if(self.king.health > 0):
            if(self.king.health > 0):
                self.board[self.king.xpos][self.king.ypos] = 1
        count_troops = 0
        count_building = 0
        for i in range(variables.ROWS):
            for j in range(variables.COLS):
                if(self.board[i][j] == 1 or self.board[i][j] == 7):
                    count_troops += 1
                if(self.board[i][j] == 4 or self.board[i][j] == 5 or self.board[i][j] == 3):
                    count_building += 1
                if(self.board[i][j] == 4 or self.board[i][j] == 5 or self.board[i][j] == 3 or self.board[i][j] == 7):
                    continue
                else:
                    self.printBoard[i][j] = printing_purpose[self.board[i][j]]
        f = open(file_name, "a")
        for i in range(variables.ROWS):
            for j in range(variables.COLS):
                f.write(self.printBoard[i][j])
            f.write('\n')
        f.close()
        print("\n".join(["".join(row) for row in self.printBoard]))
        king_health_bar = []
        for i in range(0, 16):
            if(i < 4*self.king.health):
                king_health_bar.append(Back.RED + ' ' + Style.RESET_ALL)
            else:
                king_health_bar.append(Back.WHITE + ' ' + Style.RESET_ALL)
        print(*king_health_bar, sep='')
        f = open(file_name, "a")
        for i in range(16):
            f.write(king_health_bar[i])
        f.write('\n')
        f.write("==")
        f.close()
        if(count_troops == 0 or count_building == 0):
            if(count_troops == 0):
                f = open(file_name, "a")
                f.write("Defeat")
                f.write('\n')
                f.close()
                print("Defeat")
            else:
                f = open(file_name, "a")
                f.write("Victory")
                f.write('\n')
                f.close()
                print("Victory")
            return True
        else:
            print("\033[%d;%dH" % (0, 0))
            return False
        

    def RenderBarbarian(self):
        for i in self.barbarian:
            if(i.health>0):
                self.board[i.xpos][i.ypos] = 7
                if(i.health<=1 and i.health>0.5):
                    self.printBoard[i.xpos][i.ypos] = printing_purpose[7][0]
                else:
                    self.printBoard[i.xpos][i.ypos] = printing_purpose[7][1]

    def RenderWalls(self):
        for i in self.wall:
            if(i.health > 0):
                self.board[i.xpos][i.ypos] = 2

    def RenderSpawning(self):
        for i in self.spawning:
            self.board[i.xpos][i.ypos] = 6

    def RenderCannon(self):
        for i in self.cannon:
            if(i.health>0):
                self.board[i.xpos][i.ypos] = 3
                if(i.shoot):
                    self.printBoard[i.xpos][i.ypos] = printing_purpose[3][1]
                else:
                    self.printBoard[i.xpos][i.ypos] = printing_purpose[3][0]


    def RenderTownHall(self):
        xpos = self.townhall.xpos
        ypos = self.townhall.ypos
        if(self.townhall.health>0 and self.townhall.health<=2):
            for i in range(4):
                for j in range(3):
                    self.board[i+xpos][j+ypos] = 4
                    self.printBoard[i+xpos][j+ypos] = printing_purpose[4][2]
        if(self.townhall.health>2 and self.townhall.health<=5):
            for i in range(4):
                for j in range(3):
                    self.board[i+xpos][j+ypos] = 4
                    self.printBoard[i+xpos][j+ypos] = printing_purpose[4][1]
        if(self.townhall.health>5 and self.townhall.health<=10):
            for i in range(4):
                for j in range(3):
                    self.board[i+xpos][j+ypos] = 4
                    self.printBoard[i+xpos][j+ypos] = printing_purpose[4][0]

    def RenderHuts(self):
        for i in self.huts:
            if (i.health > 0 and i.health<=1):
                self.board[i.xpos][i.ypos] = 5
                self.printBoard[i.xpos][i.ypos] = printing_purpose[5][2]
            if (i.health > 1 and i.health<=2.5):
                self.board[i.xpos][i.ypos] = 5
                self.printBoard[i.xpos][i.ypos] = printing_purpose[5][1]
            if (i.health > 2.5 and i.health<=5):
                self.board[i.xpos][i.ypos] = 5
                self.printBoard[i.xpos][i.ypos] = printing_purpose[5][0]

    def RenderWallRows(self, xinit, y, xfinal):
        for i in range(xinit, xfinal):
            self.board[i][y] = 2

    def RenderWallsCols(self, yinit, x, yfinal):
        for i in range(yinit, yfinal):
            self.board[x][i] = 2
