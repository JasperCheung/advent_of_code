from sys import stdin
from collections import deque, defaultdict as dd, Counter
import heapq as hq
import math
import itertools as it
import bisect
from copy import deepcopy as dcpy
from functools import reduce
from collections.abc import Iterable

def flatten_g(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def flatten(l):
    return list(flatten_g(l))

rl = stdin.readline
rls = stdin.readlines
bsl = bisect.bisect_left
bsr = bisect.bisect_right

sz = 20
grid = [[[["."]*sz for i in range(sz)] for j in range(sz)] for k in range(sz)]
ans = 0

lines = stdin.read().strip().splitlines()


for y in range(6,6+len(lines)):
    for x in range(6,6+len(lines[0])):
        grid[sz//2][sz//2][y][x] = lines[y-6][x-6]

#  for r in grid[sz//2]:
    #  print(r)
#  quit()

for i in range(6):
    print(i)
    grid2 = dcpy(grid)
    for w in range(sz):
        for z in range(sz):
            for y in range(sz):
                for x in range(sz):
                    a = 0
                    for dw in range(-1,2):
                        for dz in range(-1,2):
                            for dy in range(-1,2):
                                for dx in range(-1,2):
                                    nw,nz,ny,nx = w+dw,z+dz,y+dy,x+dx

                                    if (nw,nz,ny,nx)!=(w,z,y,x) and (0<=nw<sz) and (0<=nz<sz) and (0<=ny<sz) and (0<=nx<sz) and grid[nw][nz][ny][nx] == "#":
                                        a += 1

                    if grid[w][z][y][x] == "#":
                        if 2<=a<=3:
                            grid2[w][z][y][x] = "#"
                        else:
                            grid2[w][z][y][x] = "."

                    if grid[w][z][y][x] == ".":
                        if 3<=a<=3:
                            grid2[w][z][y][x] = "#"
                        else:
                            grid2[w][z][y][x] = "."

    grid = dcpy(grid2)
print( flatten(grid).count("#") )


# parts = rl().strip().split(",")
#  for i in range(len(parts)):
    #  part = parts[i]

#  print(  )


#  groups = stdin.read().strip().split("\n\n")
#  for g in groups:
    #  lines = g.splitlines()
    #  for line in lines:
        #  a,b = line.split(",")

#  print(  )
