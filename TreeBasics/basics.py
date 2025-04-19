'''
pre order traversal : DLR
in order Traversal : LDR
post order Traversal: LRD
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

# TC: O(N), we are visiting every node only once , so O(N)
# SC : O(H), H being the height, 


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

# TC : O(N), we are visiting every node only once
# SC : O(H), H being the height of the tree

def postorder(root):
    if root.data == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

# TC : O(N), we are visiting every node only once
# SC : O(H), H being the height of the tree