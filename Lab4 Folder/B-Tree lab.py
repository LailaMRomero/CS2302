"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 4
03/24/19

this code contains the methods for finding the height of the B-Tree, printing 
the elements at a certain depth of the tree, depth of certain element, number 
of elements in depth, Largest at depth, smallest at depth,Number of full leaves,
and number of full nodes
"""
class BTree(object):
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
def Search(T,k):
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
def LargestAtDepth(T,d):
    if d==0:
        return T.item[-1]
    if T.isLeaf:
        return None
    return LargestAtDepth(T.child[-1],d-1)
def SmallestAtDepth(T,d):
    if d==0:
        return T.item[0]
    if T.isLeaf:
        return None
    return SmallestAtDepth(T.child[0],d-1)

def PrintAtDepth(T,d):
    if d==0:
        for t in T.item:
            print(t,end=' ')
    if not T.isLeaf:
        for i in range(len(T.child)):
            PrintAtDepth(T.child[i],d-1)
def NodesAtDepth(T,d): 
    if d==0:
        return len(T.item)
    if not T.isLeaf:
        return NodesAtDepth(T.child[0],d-1)+NodesAtDepth(T.child[-1],d-1)

def FindDepth(T, k): # Returns the depth of item k in b-tree with root T, or -1 if
# k is not in the tree
    if k in T.item:
        return 0
    if T.isLeaf:
        return -1
    if k>T.item[-1]:
        d = FindDepth(T.child[1],k)
    else:
        for i in range(len(T.item)):
            if k < T.item[i]:
                d = FindDepth(T.child[i],k)
    if d==-1:
        return -1
    return d + 1
def FullNodes(T):
    count =0
    if len(T.item) == T.max_items:
        count += 1
    return count

def FullLeaf(T):
    count =0
    if not T.isLeaf:
        return 0
    else:
        if len(T.isLeaf)==T.max_items:
            count+=1    
    return count

L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 
     200, 2, 45, 6]
T = BTree()    
for i in L:
    Insert(T,i)
    
D =1
elem =3
print("Elements at depth: ",D)
print(PrintAtDepth(T, D))
print("Depth of Element ", elem, ":", FindDepth(T,elem))
print("Num Elements at depth ", D, ":", NodesAtDepth(T,D)) 
print("Largest:", LargestAtDepth(T,D))
print("Smallest:", SmallestAtDepth(T,D))
print("Height of Tree:", height(T))
print("Number of Full Leaves: ", FullLeaf(T))
print("Number of Full Nodes:", FullNodes(T))