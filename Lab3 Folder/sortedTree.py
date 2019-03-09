"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 3
03/08/19

this code contains the methods for the sorred array and for the depths of the keys
for the tree it sorts the array by splitting it to the array in half and traverses 
through the array. it then prints out the tree in pre-order
The key depths will indiciate the levels of the nodes and prints the keys starting at depth 0
"""

class Node: 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
  
def sortedArrayToBST(T): 
    if not T: 
        return None
    mid = (len(T)) // 2
    root = Node(T[mid]) 
    root.left = sortedArrayToBST(T[:mid]) 
    root.right = sortedArrayToBST(T[mid+1:]) 
    return root 
def preOrder(node): 
    if not node: 
        return
    print( node.data, end=' ') 
    preOrder(node.left) 
    preOrder(node.right)
    
def LevelOrder(root): 
    h = height(root) 
    for i in range(0, h+1): 
        print()
        print("Keys at depth", i, ": ", end= ' ')
        Level(root, i) 
def Level(root , level): 
    if root is None: 
        return
    if level == 0: 
        print(root.data) 
    elif level > 0 : 
        Level(root.left , level-1) 
        Level(root.right , level-1) 

def height(node): 
    if node is None: 
        return 0 
    else :        # height of each subtree  
        left = height(node.left) 
        right = height(node.right) 
        if left > right : 
            return left+1
        else: 
            return right+1
    
T = [10,4,2,1,3,7,5,9,8,15,12,18] 
root2=sortedArrayToBST(T) 
print("PreOrder: ")
print(preOrder(root2)) 
print(LevelOrder(root2))



  