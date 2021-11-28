from copy import deepcopy as dcpy
from sys import stdin
from collections import deque, defaultdict as dd, Counter
import heapq as hq
import math
import itertools as it
import bisect
from copy import deepcopy as dcpy
from functools import reduce
from collections.abc import Iterable
def part_1():
    ret = 0
    with open('input.txt', 'r') as file:

        data  = file.read()

    return game_of_life(data)


def game_of_life(data):
    # z, y, x
    sz = 20

    grid = [[["." for i in range(sz)] for i in range(sz)] for i in range(sz)]
    data = data.split("\n")
    sd = len(data[0])
    new_d = []
    # populate the grid
    for line in data:
        if(line != "\n" and  line != ""):
            new_d.append([c for c in line.strip()])

    for y in range(6,len(new_d) + 6):
        for x in range(6,len(new_d[0]) + 6):
            grid[sz//2][y][x] = new_d[y-6][x-6]
    #start the simulation
    for i in range(6):
        how_many = 0
        tmp = dcpy(grid)
        for z in range(sz):
            for y in range(sz):
                for x in range(sz):
                    a = 0
                    #check neighbors
                    for d_z in range(-1,2):
                        for d_y in range(-1,2):
                            for d_x in range(-1,2):
                                nz, ny, nx = d_z + z ,d_y + y,d_x + x

                                if((nz,ny,nx) != (z,y,x) and (0<=nz<sz) and (0<=ny<sz) and (0<=nx<sz) and grid[nz][ny][nx] == "#"):
                                    a += 1
                    if(grid[z][y][x] == "#"):
                        if(a == 2 or a == 3):
                            how_many += 1
                            tmp[z][y][x] = "#"
                        else:
                            tmp[z][y][x] = "."
                    else:
                        if(a == 3):
                            how_many += 1
                            tmp[z][y][x] = "#"
                        else:
                            tmp[z][y][x] = "."
        grid = tmp
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(len(grid[0][0])):
                if(grid[i][j][k] == "#"):
                    ans += 1
    return ans

def part_2():
    ret = 0
    with open('3.in', 'r') as file:

        data  = file.read()

    return game_of_life_4(data)


def game_of_life_4(data):
    # z, y, x
    sz = 20

    grid = [[[["." for i in range(sz)] for i in range(sz)] for i in range(sz)] for i in range(sz)]
    data = data.split("\n")
    sd = len(data[0])
    new_d = []
    # populate the grid
    for line in data:
        if(line != "\n" and  line != ""):
            new_d.append([c for c in line.strip()])
    for y in range(6,len(new_d) + 6):
        for x in range(6,len(new_d[0]) + 6):
            grid[sz//2][sz//2][y][x] = new_d[y-6][x-6]
    #start the simulation
    for i in range(6):
        print(i)
        tmp = dcpy(grid)
        for w in range(sz):
            for z in range(sz):
                for y in range(sz):
                    for x in range(sz):
                        a = 0
                        #check neighbors
                        for d_w in range(-1,2):
                            for d_z in range(-1,2):
                                for d_y in range(-1,2):
                                    for d_x in range(-1,2):
                                        nw, nz, ny, nx = d_w + w, d_z + z ,d_y + y,d_x + x

                                        if((nw,nz,ny,nx) != (w,z,y,x) and (0<=nw<sz) and  (0<=nz<sz) and (0<=ny<sz) and (0<=nx<sz) and grid[nz][ny][nx] == "#"):
                                            a += 1
                        if(grid[w][z][y][x] == "#"):
                            if(a == 2 or a == 3):
                                tmp[w][z][y][x] = "#"
                            else:
                                tmp[w][z][y][x] = "."
                        else:
                            if(a == 3):
                                tmp[w][z][y][x] = "#"
                            else:
                                tmp[w][z][y][x] = "."
        grid = tmp

    return flatten(grid).count("#")



def flatten_g(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def flatten(l):
    return list(flatten_g(l))





print(part_1())
print(part_2())
