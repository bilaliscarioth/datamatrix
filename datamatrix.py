"""
    matrix.py
    Copyright (C) 2022  BILAL EMOHMADIAN

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""

from tkinter import *

AXE_X = 1
AXE_Y = 0

class DMatrix:
    def __init__(self, x, y):
        self.mat = [[0 for x in range(x)] for y in range(y)]

    def get(self):
        return self.mat

    def print(self):
        print("+---+---+---+---+---+---+---+---+")
        for x in range (len(self.mat)):
            for y in range (len(self.mat[x])):
                print('|', self.mat[y][x], end=" ")
            print("|\n+---+---+---+---+---+---+---+---+")


    def setWord(self, n, bytes):
        global AXE_X, AXE_Y


        index = [4, 0]

        AXE_Y, AXE_X = 0 , 1

        while((n-1) >= 0):
            if (index[AXE_Y] == 0):
                    index[AXE_Y] += 1
                    index[AXE_X] += 3
                    AXE_Y, AXE_X = AXE_X , AXE_Y
                    n -=1
            elif(index[AXE_X] == 7):
                index[AXE_X] -= 1
                index[AXE_Y] -= 3
                n -=1
            else:
                index[AXE_X] += 2
                index[AXE_Y] -= 2
                n -=1

        print(index, AXE_X, AXE_Y)
        self.mat[index[AXE_Y]][index[AXE_X]] = 1

mat = DMatrix(8,8)
for i in range (0,8):
    mat.setWord(i, 1)
mat.print()

master = Tk()

w = Canvas(master, width=500, height=750)

""" Standard """
for y in range(10):
    for x in range(10):
        w.create_rectangle(0, 50*x, 50, 50*(x+1), fill="black", outline = 'white')

        if(x%2 == 0):
            w.create_rectangle(50*x, 0, 50*(x+1), 50, fill="black", outline = 'white')
            w.create_rectangle(50*y, 50*(x-1), 50*(y+1), 50*(x), fill="black", outline = 'white')
        else:
            w.create_rectangle(50*x, 0, 50*(x+1), 50, fill="white", outline = 'black')
            w.create_rectangle(50*y, 50*(x-1), 50*(y+1), 50*(x), fill="white", outline = 'black')

        w.create_rectangle(50*y, 50*x, 50*(y+1), 50*(x+1), fill="black", outline = 'white')

""" Emplacement des Codes Matrix """
for y in range(1, 9):
    for x in range(1, 9):
        if(mat.get()[y-1][x-1]):
            w.create_rectangle(50*y, 50*x, 50*(y+1), 50*(x+1), fill="black", outline = 'white')
        else:
            w.create_rectangle(50*y, 50*x, 50*(y+1), 50*(x+1), fill="white", outline = 'black')
w.pack()
master.mainloop()
