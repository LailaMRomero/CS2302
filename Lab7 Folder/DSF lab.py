"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 7
04/30/19

This code creates a randomized maze through a disjoint set forest and takes user
input to remove walls. It then generate the adjacency list of the maze
it also uses breadth first and depth first search to solve the maze
"""
import matplotlib.pyplot as plt
import numpy as np
import random 
from scipy import interpolate
import queue

def BFS(G,v):
    visited = np.zeros(len(G), dtype=bool)
    prev=np.zeros(len(G),dtype=np.int)-1    
    q = queue.Queue()
    q.put(v)
    visited[v] = True
    while not q.empty():
        u = q.get()
        for i in G[u]:
            if not visited[i]:
                visited[i]=True
                prev[i]=u
                q.put(i)
    #print('Breadth First Solution: ')
    return prev

def dfsrec(G, source):
    global visited
    global prev
    visited[source]=True
    for t in G[source]:
        if not visited[t]:
            prev[t]=source
        dfs(G,t)
        
def dfs(G,v):
    visited = []
    stack = [v]
    while stack != []:
        current=stack.pop()
        
        for i in G[current]:
            if i not in visited:
                stack.append(i)
            visited.append(current)
    print('Depth First Search Stack: ')
    return visited

#def depth_first_search_recursive(G, v, visited=None):
#    if visited is None:
#        visited = set()
#    visited.add(v)
#    for next in G[v] - visited:
#        depth_first_search_recursive(G, next, visited)
#    return visited
    
def printPath(prev,v):
    if prev[v] != -1:
        printPath(prev,prev[v])
        print('-')
    print(v)
def printPath2(prev,v):
    q = queue.Queue()
    q.put(v)
    while not q.empty():
        u = q.get()
        for i in prev[u]:
            if prev[v] != -1:
                prev[i]=u
                q.put(i)
                print('-')
    #print('Breadth First Solution: ')
    

#def printPath(prev):
#    path =[]
#    for i in range(len(prev)-1):
#        path[i]= prev[-1]
#        path[i+1]=prev[prev[-1]]
#    return path
            

    
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def draw_dsf(S):
    scale = 10000
    fig, ax = plt.subplots()
    for i in range(len(S)):
        if S[i]<0: # i is a root
            ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
            ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
        else:
            x = np.linspace(i*scale,S[i]*scale)
            x0 = np.linspace(i*scale,S[i]*scale,num=5)
            diff = np.abs(S[i]-i)
            if diff == 1: #i and S[i] are neighbors; draw straight line
                y0 = [0,0,0,0,0]
            else:      #i and S[i] are not neighbors; draw arc
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interpolate.interp1d(x0, y0, kind='cubic')
            y = f(x)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0[2]+2*np.sign(i-S[i]),x0[2],x0[2]+2*np.sign(i-S[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)

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
    
def draw_path(walls,maze_rows,maze_cols,G, cell_nums):
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
                for i in range(len(G)):
                    if G[i] != -1:
                        ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
        
    ax.axis('off') 
    ax.set_aspect(1.0)

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

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])
def union(S,i,j):
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
        
def MazeNorm(S,walls,choice,cells): 
    G = [ [] for i in range(cells) ]
    if choice<=cells-1:
        while NumSets(S)>1 and choice > 0:
            d = random.randint(0,(len(walls)-1))
            if find(S,walls[d][0])!= find(S,walls[d][1]):
                union(S,walls[d][0],walls[d][1])
                poppedWalls=walls.pop(d)
                choice -=1    
                G[poppedWalls[1]].append(poppedWalls[0]) 
                G[poppedWalls[0]].append(poppedWalls[1]) 
    elif choice> len(walls):
        print("Not possible")
        return None

    elif choice > cells-1:
        while choice>0:
                d = random.randint(0,(len(walls)-1))
                poppedWalls=walls.pop(d)
                G[poppedWalls[1]].append(poppedWalls[0]) 
                G[poppedWalls[0]].append(poppedWalls[1]) 
                choice -=1
    print('Adjacency List: ')
    return G


plt.close("all") 
maze_rows = 3
maze_cols = 3
cells = maze_rows*maze_cols
walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)
print('The number of cells (n) is: ', cells)
print('Available walls (m): ', len(walls))
print('How many walls (m) would you like to remove?' )
choice = int(input("Walls to remove: "))
if choice > len(walls):
    print("Selection is larger than available walls")
elif choice < cells-1:
    print("A path from source to destination is not guaranteed to exist (when m < n-1)") 
elif choice == cells-1:
    print('There is a unique path from source to destination (m = n-1)')
else:
    print('There is at least one path from source to destination (m > n-1)')

print('\n')
G=MazeNorm(S,walls,choice,cells)
prev=np.zeros(len(G),dtype=np.int)-1
visited = np.zeros(len(G), dtype=bool)
print(G)
print('\n')
print('Breadth First Search: ')
print(BFS(G,0))
print(dfs(G,0))
#print(depth_first_search_recursive(G,0))
previous = BFS(G,0)
#print(previous)

#printPath2(previous,0)
#dfs(G,0)
#print(visited)
#print(prev)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
draw_path(walls,maze_rows,maze_cols,G, cell_nums=True)
