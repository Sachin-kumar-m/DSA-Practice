'''given a linked list , inset a new node with data v at index p'''

class Node:
    def __init__(self,x):
        self.x = x
        self.next = None

def linkedList(n):
    head = Node(1)
    l = head
    for i in range(2,n+1):
        l.next = Node(i)
        l = l.next
    return head
h = linkedList(6)
d = 60
p = 3

def insert(head,d,p):
    t = head
    n = Node(d)
    # handling edge case for inserting for 0th index
    if p == 0:
        n.next = t
        head = n
        return head
    for i in range(p-1):
        t = t.next
   
    n.next = t.next
    t.next = n
    # printing whole linked list
    t = head
    while t!=None:
        print(t.x)
        t = t.next
    return head
insert(h,d,p)

