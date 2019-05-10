"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 5
05/09/19

This code takes a set of integers and determines if it can be divided into two 
equal subsets. The sums of the subsets must be equal.
"""
def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]   
    
def findPartition (a): 
    suma = 0
    if len(a) ==0:      #cant partition empty set
        return "Empty set" 
    for i in range(len(a)): 
        suma += a[i]        #calculates the sum of the set
    if a[-1] > suma-a[-1]:  #if the last element is greater than sum of other elements it cant be partitioned
        return "Can not be partitioned" 
    elif (suma % 2) != 0: 
        return "Can not be partitioned" 
    else:
        res, S=(subsetsum(a,len(a)-1, suma//2))  # finds the first set through subset sum
        for i in range(len(S)):                 #pops whatever is in the subset out original set
            if S[i] in a:
                a.pop(a.index(S[i]))
        return a, S
                                    #returns both sets
a = [2,4,5,9,12]
b = [2,4,5,9,13]
print(findPartition(a))
print(findPartition(b))
