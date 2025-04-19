'''
given a root of the tree, return height of the tree
'''

def height_of_tree(root):
    if root == None:
        return -1
    return 1+(max(height_of_tree(root.left),height_of_tree(root.right)))

