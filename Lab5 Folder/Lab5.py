"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 5
04/01/19

this code reads in the the glove file and sorts the numbers into either a hashtable
or binary search tree. It will also read in the file that compare the two names 
"""

def Options(choice):
    if choice == 1:
        print("Building binary search tree")
    if choice ==2:
        print("Building hash table with chaining")
    if choice is not 1 or 2:
        return 
 
def numLines(fileName):
    count =0
    with open(fileName, 'rb') as f:
        for line in f:
            count +=1
    return count

def BigList(numLines, text):
    newFile= open(text, encoding='utf-8')
    newList= [None]*numLines
    for i in range(numLines):
        newList[i]=newFile.readline()
    return newList

def listMaker(theList):
    newList=[]
    for i in range (len(theList)):
        innerList = theList[i].split(" ",1)
        innerListNums = innerList[0].split(" ", 50)
        for j in range (len(innerListNums)):
            innerListNums[j]= float(innerListNums[j])
        newList.append([innerList[1], innerListNums])
    return newList
        
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
        r = (r*k + ord(c))% n
    return r
def spaces(fileName):
     new_items = []
     for item in fileName:
         new_items.extend(item.split(' ',1))
     return new_items
 
def spaces2(fileName):
    newList=[]
    for i in fileName:
        innerList = fileName.split(" ",1)
        innerListNums = innerList[1].split(" ", 50)
        for j in range (len(innerListNums)):
            innerListNums[j]= float(innerListNums[j])
        newList.append([innerList[0], innerListNums])
    return newList

def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

H = HashTableC(50)
print("Choose table implementation")
print("Type 1 for binary search tree or 2 for hash table with chaining")
choice = int(input("Choice: "))
print(Options(choice))

path = 'C:/Users/lmrs8/Documents/glove.6B.50d.txt'
text_file=open(path, encoding= "utf-8")
text_file=open(path, 'r')
text_file=open(path, errors='ignore')
text=text_file.readline()
#print(text)

pathC = 'C:/Users/lmrs8/Documents/comparisons.txt'
C_file=open(pathC, encoding= "utf-8")
C_file=open(pathC, 'r')
C_file=open(pathC, errors='ignore')
comp=C_file.readlines()
print(comp)
print(spaces(comp))
print(spaces2(text))
print("Number of lines in the file: ",file_lengthy("comparisons.txt"))        
#print(listMaker(text))
#print(BigList(num_lines(text),text))
text_file.close()
fname = text_file
num_lines = 0
#with open(fname, 'rt') as f:
 #   for line in f:
  #      num_lines += 1
#print(BigList(num_lines,text))

#rint("Number of lines:")
#print(num_lines)   
       
