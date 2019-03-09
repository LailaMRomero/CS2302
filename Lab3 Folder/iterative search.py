"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 3
03/08/19

this code contains the method for the iterative binary search by taking the 
middle of the array and traversing through the array and searching for the 
designated element and returnss the index of where the element is found
"""
def binarySearch(T, l, j, x):  
    while l <= j: 
        mid = l + (j- l)//2;           
        if T[mid] == x: 
            return mid 
        elif T[mid] < x: 
            l = mid + 1
        else: 
            j = mid - 1
    return -1
T = [1, 2, 3, 4, 5, 7,8,9,10,12,15,18] 
x = 10
result = binarySearch(T, 0, len(T)-1, x) 
if result != -1: 
    print("Element is at index", result) 
else: 
    print("Element is not in array")