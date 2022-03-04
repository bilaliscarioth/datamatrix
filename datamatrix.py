"""
    matrix.py
    Copyright (C) 2022  BILAL EMOHMADIAN
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from tkinter import *
from typing import (
    List
)

AXE_X = 1
AXE_Y = 0

def define_codwords(n:int) -> List[int]:
    """
    Give n: int
    ____
    Return a list of bits.
    """
    list = []
    while(n > 0):
        bit = n %2
        n = n // 2
        list.append(bit)
    return list[::-1]

class DMatrix:
    def __init__(self, x, y):
        self.mat = [[0 for x in range(x)] for y in range(y)]

    def get(self):
        return self.mat

    def reed_solomon(bytes: List[int]) -> List[int]:
        try:
            list = []

            return list
        except Exception as e:
            return []

    def print(self):
        print("+---+---+---+---+---+---+---+---+")
        for x in range (len(self.mat)):
            for y in range (len(self.mat[x])):
                print('|', self.mat[y][x], end=" ")
            print("|\n+---+---+---+---+---+---+---+---+")

    def placeCodeWords(self, y:int, x:int, data:List[int]) -> None:
        """ 
        y: index of the first table
        x: index of the second table
        data: list of bits
        """

        global AXE_X, AXE_Y

        if(AXE_X == 0 and AXE_Y == 1):
            x ,y  = y, x

        #find  a better way to upgrade this

        self.mat[y][x] = data[7]      #   8th bit
        self.mat[y-1][x] = data[6]    #   7th bit
        self.mat[y-2][x] = data[5]    #   6th bit

        self.mat[y][x-1] = data[4]      #   5th bit
        self.mat[y-1][x-1] = data[3]    #   4th bit
        self.mat[y-2][x-1] = data[2]    #   3rd bit

        self.mat[y-1][x-2] = data[1]    #   2nd bit
        self.mat[y-2][x-2] = data[0]    #   1st bit

        return


    def setWord(self, n:int, bytes:int) -> None:
        """
        n: is the n-th codewords
        bytes: data storage
        __________
        Return None.
        """
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

        self.placeCodeWords(index[AXE_X], index[AXE_Y], bytes) # Inversed X <-> Y to give data in a codewords


mat = DMatrix(8,8)
bytes = [98, 76, 54]
rs = []
for i in range (0,3):
    mat.setWord(i, define_codwords(130+ bytes[i]))
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
w.grid(row=0, column=0)
master.mainloop()
