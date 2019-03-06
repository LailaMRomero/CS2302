"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 1
02/08/19

to get the circles to the left of the original circle you adjust the center of 
each circle after each recursive call by adding the radius to the x coordinate
of the center.
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

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x + radius,y,color='k') # will change the center of the new circles
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 10, [100,0], 100,.6)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
