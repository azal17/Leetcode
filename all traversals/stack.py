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
    if not root:
        return
    inorder,preorder, postorder =[], [], []
    stack = [(root, 1)]

    while stack:
        node, num = stack.pop()
        if num == 1:
            preorder.append(node.data)
            num += 1
            stack.append((node, num))

            if node.left:
                stack.append((node.left, 1))
        elif num == 2:
            inorder.append(node.data)
            num += 1
            stack.append((node, num))

            if node.right:
                stack.append((node.right, 1))
        elif num == 3:
            postorder.append(node.data)
            
            
    return inorder,preorder, postorder
