# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi = float('-inf')
    
    def path(self, node):
        if node is None:
            return 0
    
        left = max(0, self.path(node.left))  
        right = max(0, self.path(node.right))
        self.maxi = max(self.maxi, left + right + node.val)

        return max(left, right) + node.val
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path(root)
        return self.maxi
