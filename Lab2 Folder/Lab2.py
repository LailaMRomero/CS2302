"""
Laila Romero
CS 2302
Professor Olac Fuentes
Lab 2
02/22/19

this code contains methods for mergesort, bubblesort, quick sort, and finding 
the middle of the linked list

"""
class Node:
   def __init__(self,data=None,next=None):
       self.data = data
       self.next = next
   def __str__(self):
        return str(self.data)

   def printList(self):  
       print(self.data, end=' ')
       if self.next:
           self.next.printList()
       else:
           print()      
   def bubbleSort(self):
       start = self
       result = start.bubbleSortPass()   # start sorting first node
       start = result[0]
       while result[1]:
           result = start.bubbleSortPass()
           start = result[0]  # change the head
       return start
          
   def bubbleSortPass(self):    # simulates one pass of bubble sort
       if(self.next):
           nextNode = self.next
          
           # check if node need to be swapped
           if(self.data > self.next.data):
               self.next = nextNode.next               # swap the nodes
               nextNode.next = self
               result = self.bubbleSortPass()   # use for further sort
               nextNode.next = result[0]     # check if head changed
               return (nextNode, True)
           else:
               result = self.next.bubbleSortPass()
               self.next = result[0]
               return (self, result[1])
       else :
           return (self, False)
   def mergeLists(l1, l2):
        temp = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.data <= l2.data:
            temp = l1
            temp.next = mergeLists(l1.next, l2)
        else:
            temp = l2
            temp.next = mergeLists(l1, l2.next)
        return temp
    
   def mergeSort(head):
        if head == None or head.next == None:
            return head
        l1, l2 = divideLists(head)
        l1 = mergeSort(l1)
        l2 = mergeSort(l2)
        head = mergeLists(l1, l2)
        return head
    
   def divideLists(head):
        middle = head # middle is a pointer to reach the mid 
        end = head   # end is a pointer to reach the end 
        if end:
            end = end.next            
        while end:
            end = end.next   # end is incremented twice, middle 
                                #is incremented once
            if end:
                end = end.next
                middle = middle.next
        mid = middle.next
        middle.next = None
        return head, mid
def find_middle(node):
    list = []
    while node:
        list.append(node)
        node = node.next
    return "Middle node is %s" % str(list[len(list)//2])

L = Node(100,Node(96,Node(95,Node(97,Node(99,Node(98))))))
L1 = Node(123,Node(6,Node(945,Node(57,Node(67,Node(8))))))
print("Before Sort")
L.printList()
L1.printList()
L = L.bubbleSort()
L1= L1.mergeSort()
print("After sort")
L.printList()
print(find_middle(L))
L1.printList()
print(find_middle(L1))
