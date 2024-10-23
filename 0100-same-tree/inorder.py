# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# INORDER, SAME COMPLEXITY
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        
        if not self.isSameTree(p.left, q.left):
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True
