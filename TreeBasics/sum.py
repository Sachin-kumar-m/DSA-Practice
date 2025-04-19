'''
given a root of a tree, return sum of all the elements in the tree
'''


def sum_of_tree(root):
    if root == None:
        return 

    return root.data + sum_of_tree(root.left)+sum_of_tree(root.right)