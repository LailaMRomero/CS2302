"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 5
05/09/19

This code discovers the trig functions and compares them to other functions with
random integers ranging from -pi to pi. 
"""
import random
import numpy as np
import mpmath 
from math import *
from math import pi

def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        x = (2*pi*random.random())-pi
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

def equaltrig(List):  #Traverses through the list of trig functions
    for i in range(len(List)):
        for j in range(i+1, len(List)):
            if equal(List[i], List[j]):
                print(List[i], '=', List[j])
            else:
                print(List[i], '!=', List[j])
    
S = [2,4,5,9,12]
List = ['sin(x)','cos(x)','tan(x)','mpmath.sec(x)','-sin(x)', '-cos(x)', '-tan(x)', 
        'sin(-x)','cos(-x)','tan(-x)','sin(x)/cos(x)', '2*sin(x/2)*cos(x/2)', 'sin(x)**2',
        '1-(cos(x)**2)', '(1-cos(2*x))/2', '(1)/cos(x)']
equaltrig(List)
