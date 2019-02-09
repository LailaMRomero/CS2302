"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 1
02/08/19


for the tree example you start at the origin at the top of the tree then 
set the other coordinates to half of the radius of the space. You do this for 
every level then for the x coordinates and for the y coordinate you take the 
number of levels and divide it by the height of the workspace
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_nest(ax,n, x, size,levels):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k')        
        ax.plot(q[:,0],q[:,1],color='k')
        ax.plot(r[:,0],r[:,1],color='k')
        ax.plot(s[:,0],s[:,1],color='k')
        ax.plot(t[:,0],t[:,1],color='k')
        ax.plot(u[:,0],u[:,1],color='k')
        ax.plot(v[:,0],v[:,1],color='k')
        draw_nest(ax,n-1,p,size,levels)



plt.close("all") 
size = 90
n=1
levels=3
new_size= size/levels
fig, ax= plt.subplots()
p = np.array([[-new_size,-new_size],[0,0],[new_size,-new_size]])
q = np.array([[-size/2,-2*new_size],[-new_size,-new_size],[-new_size/2,-2*new_size]])
r = np.array([[new_size/2,-2*new_size],[new_size,-new_size],[new_size/2+new_size,-2*new_size]])
s = np.array([[new_size/4,-size], [new_size/2,-2*new_size],[new_size-new_size/4,-size]])
t = np.array([[-new_size/4,-size], [-new_size/2,-2*new_size],[-new_size+new_size/4,-size]])
u = np.array([[-2*new_size+ new_size/4,-size], [-new_size-new_size/2,-2*new_size], [-new_size-new_size/4,-size]])
v = np.array([[new_size+new_size/4,-size], [new_size+new_size/2, -2*new_size], [2*new_size-new_size/4,-size]])
draw_nest(ax,n,p,size,levels)

ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')

        