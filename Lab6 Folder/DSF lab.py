"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 6
04/15/19

This code creates a randomized maze through a disjoint set forest and makes sure
all the cells point to the same 
"""
import matplotlib.pyplot as plt
import numpy as np
import random 
import time
from random import shuffle, randrange

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows 
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)
    
    def walk(x, y):
        w[sy][sx] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        walk(x0, y0)

        walk(randrange(sx), randrange(sy))

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
def NumSets(S):
    num =0
    for i in range(len(S)):
        if S[i] <0:
            num+=1
    return num
        
def MazeNorm(rows,cols,S,walls):
    while NumSets(S)>1:
        d = random.randint(0,(len(walls)-1))
        if find(S,walls[d][0])!= find(S,walls[d][1]):
            union(S,walls[d][0],walls[d][1])
            walls.pop(d)
            
def MazeComp(rows,cols,S,walls):
    while NumSets(S)>1:
        d = random.randint(0,(len(walls)-1))
        if find_c(S,walls[d][0])!= find_c(S,walls[d][1]):
            union_by_size(S,walls[d][0],walls[d][1])
            walls.pop(d)

plt.close("all") 
maze_rows = 10
maze_cols = 12
walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)

start = time.time()
MazeNorm(maze_rows, maze_cols,S,walls)
draw_maze(walls,maze_rows,maze_cols) 
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
end = time.time()

startc  = time.time()
MazeComp(maze_rows, maze_cols, S, walls)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
draw_maze(walls,maze_rows,maze_cols) 
endc = time.time()
print('Running time for normal: ', end-start)
print('\n')
print('Running time for compression: ', endc-startc)

