"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 3
03/08/19

for the binary tree you use a similar technique as you did for the first lab by
plotting the points to the lines and connecting them with the other lines. to annotate the 
points and make node at the top you add text to the center of the top of the lines and 
write the number on the nodes to make the tree
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_nest(ax,n, x, size,levels):
    if n>0:
        ax.plot(p[:,0],p[:,1],color='k')  
        ax.plot(q[:,0],q[:,1],color='k')
        ax.plot(r[:,0],r[:,1],color='k')
        ax.plot(t[:,0],t[:,1],color='k')
        ax.plot(u[:,0],u[:,1],color='k')
        ax.plot(v[:,0],v[:,1],color='k')
        draw_nest(ax,n-1,p,size,levels)


plt.close("all") 
size = 100
n=10
levels=4
new_size= size/levels
fig, ax= plt.subplots()
p = np.array([[-new_size,-new_size],[0,0],[new_size,-new_size]])
q = np.array([[-new_size-new_size/2, -2*new_size],[-new_size,-new_size],[-new_size/2,-2*new_size]])
r = np.array([[new_size/2,-2*new_size],[new_size,-new_size],[new_size/2+new_size,-2*new_size]])
t = np.array([[-new_size/4,3*-size/4], [-new_size/2,-2*new_size],[-new_size+new_size/4,-3*size/4]]) #5
u = np.array([[-2*new_size+ new_size/4,-3*size/4], [-new_size-new_size/2,-2*new_size], [-new_size-new_size/4,-3*size/4]])
v = np.array([[-new_size+ 2*new_size/4,-size], [-3*new_size/4,-3*size/4]])
draw_nest(ax,n,p,size,levels)

bbox_props = dict(boxstyle="circle,pad=0.3", fc="white", ec="k", lw=2)
t = ax.text(0, 0, "10", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-new_size, -new_size, "4", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(new_size, -new_size, "15", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-new_size/2, -2*new_size, "8", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-new_size-new_size/2, -2*new_size, "2", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-2*new_size+ new_size/4,-3*size/4, "1", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-new_size-new_size/4,-3*size/4, "3", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-new_size/4,-3*size/4, "9", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-new_size+new_size/4,-3*size/4, "5", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(new_size/2,-2*new_size, "12", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(new_size/2+new_size,-2*new_size, "18", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
t = ax.text(-new_size+ 2*new_size/4,-size, "7", ha="center", va="center", rotation=0,
            size=10,bbox=bbox_props)
bb = t.get_bbox_patch()
bb.set_boxstyle("circle", pad=0.3)


ax.set_aspect(1.0)
ax.axis('on')
plt.show()
#fig.savefig('squares.png')

        