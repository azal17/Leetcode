# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lh = self.ht(root.left)
        rh = self.ht(root.right)
    
        if abs(lh - rh) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def ht(self, root):
        if root is None:
            return 0  
        lh = self.ht(root.left)
        rh = self.ht(root.right)

        return max(lh, rh) + 1