'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def isLeaf(root):
    return root.left is None and root.right is None
def leaves(root, arr):
    if root is None:
        return
    if isLeaf(root):
        arr.append(root.data)
    else:
        if root.left:
            leaves(root.left, arr) 
        if root.right:  
            leaves(root.right, arr)  
def leftBoundary(root, arr):
    curr = root.left
    while curr:

        if not isLeaf(curr):
            arr.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def rightBoundary(root, arr):
    curr = root.right
    temp = []
    while curr:

        if not isLeaf(curr):
            temp.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    temp.reverse()
    arr.extend(temp)

def traverseBoundary(root):
    if not root:
        return []
    arr = []
    if not isLeaf(root):
        arr.append(root.data)
    leftBoundary(root, arr)  
    leaves(root, arr)    
    rightBoundary(root, arr)   
    return arr