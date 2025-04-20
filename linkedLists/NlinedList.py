'''Create a linked list with n nodes, data in nodes will be numbers (1-n) and return the head node'''

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
print(linkedList(n))    

a = linkedList(n)
def size(n):
    ans = 0
    h = n
    while h!=None:
        ans+=1
        h = h.next
    return ans
print(size(a))
