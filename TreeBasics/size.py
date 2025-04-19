'''
given root of the tree, determine how many elements are present in the tree
'''


def size(root):
    if root == None:
        return
    return 1+size(root.left)+size(root.right) 