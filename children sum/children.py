from os import *
from sys import *
from collections import *
from math import *

'''

    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
        
def changeTree(root): 
    if not root:
        return
    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data

    if child >= root.data:
        root.data = child
    else:
        if root.left:
            root.left.data = root.data
        elif root.right:
            root.right.data = root.data
    changeTree(root.left)
    changeTree(root.right)

    check = 0

    if root.left:
        check += root.left.data
    if root.right:
        check += root.right.data
    if root.left or root.right:
        root.data = check


            
