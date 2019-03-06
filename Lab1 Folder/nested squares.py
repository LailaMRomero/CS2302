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
        ax.plot(u[:,0],u[:,1],color='k')
        ax.plot(v[:,0],v[:,1],color='k')  
        ax.plot(w[:,0],w[:,1],color='k') 
        ax.plot(x[:,0],x[:,1],color='k')  
        ax.plot(y[:,0],y[:,1],color='k')              
        draw_nest(ax,n-1, u, point)
        draw_nest(ax,n-1, v, point)
        draw_nest(ax,n-1, w, point)
        draw_nest(ax,n-1, x, point)
        draw_nest(ax,n-1, y, point)

plt.close("all") 
size = 100
point = size/4
n=1
u = np.array([[0,0],[0,size],[size,size],[size,0],[0,0]])
v = np.array([[point*3,-point],[point*3,point],[size+point,point],[size+point,-point],[point*3,-point]])
w = np.array([[-point,-point],[-point,point],[point,point],[point,-point],[-point,-point]])
x = np.array([[-point, size+point],[point, size+point],[point, size-point],[-point,size-point], [-point, size+point]])
y = np.array([[size-point, size+point],[size+point, size+point],[size+point, size-point],[size-point,size-point], [size-point, size+point]])

fig, ax = plt.subplots()
draw_nest(ax,n, u, point)
draw_nest(ax,n, v , point)
draw_nest(ax,n, w , point)
draw_nest(ax,n, x, point)
draw_nest(ax,n, y, point)

ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')

        
