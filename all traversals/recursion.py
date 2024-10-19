from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    inorder_array = []
    preorder_array = []
    postorder_array = []
    def allorders(root):
        if not root:
            return
        preorder_array.append(root.data)
        allorders(root.left)
        inorder_array.append(root.data)
        allorders(root.right)
        postorder_array.append(root.data)
    allorders(root)
    return inorder_array,  preorder_array, postorder_array



    