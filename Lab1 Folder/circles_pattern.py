"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 1
02/08/19

for the multiple circles you take the center of the main circle then divide the
diameter by 3 to get the new centers for the circles inside of it. then call 
recursive method
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius)
        draw_circles(ax,n-2, center, radius/3)

plt.close("all") 
fig, ax = plt.subplots() 
radius=100
center= [0,0]
draw_circles(ax, 3, center, radius)
draw_circles(ax, 3, [-2*radius/3,0], radius)
draw_circles(ax, 3, [2*radius/3,0], radius)
draw_circles(ax, 3, [0,2*radius/3], radius)
draw_circles(ax, 3, [0,-2*radius/3], radius)

ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')
