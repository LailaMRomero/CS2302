import time
import math

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

         
def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def Find(T,k):
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    

class HashTableC(object):
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
def InsertC(H,k,l):
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def similarity(H,w1,w2):
    ww1 = FindC(H,w1)
    ww2=FindC(H,w2)
    top = 0
    bottom_a=0
    bottom_b=0
    for i in range(len(ww1)):
        top += float(ww1[i])*float(ww2[i])
        bottom_a += float(ww1[i])**2
        bottom_b += float(ww2[i])**2
    bottom_a=math.sqrt(bottom_a)
    bottom_b=math.sqrt(bottom_b)
    return top/(bottom_a*bottom_b)

def reCompute(H):
    temp = HashTableC(len(H.item))
    for i in range(len(H.item)):
        for j in range (len(H.item[i])):
            InsertC(temp,H.item[i][j][0], H.item[i][j][1])
    return temp

def BigList(numLines, text):
    newFile= open(text, encoding='utf8')
    newList= [None]*numLines
    for i in range(numLines):
        newList[i]=newFile.readline()
    return newList
    print('', end='\n' )

def listMaker(theList):
    newList=[]
    for i in range (len(theList)):
        innerList = theList[i].split(" ",1)
        innerListNums = innerList[0].split(" ")
        for j in range (len(innerListNums)):
            innerListNums[j]= float(innerListNums[j])
        newList.append([innerList[1], innerListNums])
    return newList

def spaces2(fileName):
    newList=[None]
    for i in range(1):
        innerList = fileName.split(" ",1)
        innerListNums = innerList[1].split(" ")
        for j in range (len(innerListNums)):
            innerListNums[j]= float(innerListNums[j])
        newList.append([innerList[0], innerListNums])
    return newList

def doubleSize(H):
    H2=HashTableC(len(H.item)*2+1)
    for b in range(len(H.item)):
        for i in H.item[b]:
            InsertC(H2,i)
    return H2
def Percentage(H):
    j=0
    for i in range(len(H.item)):
        if len(H.item[i]==0):
            j=j+1
    return j/len(H.item)*100
path = 'C:/Users/lmrs8/Documents/glove.6B.50d.txt'
text_file=open(path, encoding= "utf-8")
text_file=open(path, 'r')
text_file=open(path, errors='ignore')
text=text_file.readline()

T = None
A = spaces2(text)
for a in A:
   # T = Insert(T,a)
   print(end='\n')
InOrder(T)

file = 'glove.6B.50d.txt'
size = 11
H = HashTableC(size)
print("Choose table implementation")
print("Type 1 for binary search tree or 2 for hash table with chaining")
choice = int(input("Choice: "))
if choice ==1:
    print("building binary search tree")
    start = time.time()
    Hre= reCompute(H)
    print(end='\n')
    print('Reading word file to determine similarities')
    with open("comparisons.txt") as compares:
        for line in compares:
            string2 = line.split()
            print(end='\n')
            print(string2[0]+" "+string2[1]+ " ")
            print(str(similarity(Hre, string2[0], string2[1])))
            print(end='\n')
    end=time.time()
    print('Running Time', end-start)
    
if choice ==2:
    start = time.time()
    print("building hash table")
    print(spaces2(text))
    Hre= reCompute(H)
    print(end='\n')
    print('Initial size ', size)
    print('New Size ', len(H.item)*2+1)
   # print(Percentage(H))
    print(end='\n')
    print('Reading word file to determine similarities')
    with open("comparisons.txt") as compares:
        for line in compares:
            string2 = line.split()
            print(end='\n')
            print(string2[0]+" "+string2[1]+ " ")
            print(str(similarity(Hre, string2[0], string2[1])))
            print(end='\n')
    end=time.time()
    print('Running Time', end-start)