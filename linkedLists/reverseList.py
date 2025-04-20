'''
given a linked list, you need to print the linked list in a reverse order
'''


class Node:
    def __init__(self,x):
        self.x = x
        self.next = None
    
n = 5

def linkedList(n):
    head = Node(1)
    l = head
    for i in range(2,n+1):
        l.next = Node(i)
        l = l.next
    return head


linkedList = linkedList(n) 


print(linkedList)


def printList(node):
    if node==None:
        return
    
    printList(node.next)
    print(node.x)
printList(linkedList)