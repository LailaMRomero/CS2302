"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 1
02/08/19

the squares use the vertices of the larger square as center points which can be
achieved by dividing the size of the original square by 4. Then use this as the
new center point for the smaller squares and manipulate the x and y cooridinates
to align them on the corners
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_nest(ax,n, x, point):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k')
        ax.plot(x[:,0],x[:,1],color='k')  
        ax.plot(x[:,0],x[:,1],color='k')      
        draw_nest(ax,n-1, p, point)

plt.close("all") 
size = 100
point = size/4
n=1
p = np.array([[0,0],[0,size],[size,size],[size,0],[0,0]])
v = np.array([[point*3,-point],[point*3,point],[size+point,point],[size+point,-point],[point*3,-point]])
fig, ax = plt.subplots()
draw_nest(ax,n, x, point)
draw_nest(ax,n, v , point)
draw_nest(ax,n, y , point)
draw_nest(ax,n, z , point)

ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')

        