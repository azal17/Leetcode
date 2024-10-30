# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        child = 0
        if root.left:
            child += root.left.val
        if root.right:
            child += root.right.val
        
        if root.val == child:
            return True if self.checkTree(root.left) and self.checkTree(root.left) else False
        else:
            return False
