# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  
        def findmax(node):
            if node is None:
                return 0  
            lh = findmax(node.left)
            rh = findmax(node.right)
            self.max_diameter = max(self.max_diameter, lh + rh)
            return 1 + max(lh, rh)
        
        findmax(root)  
        return self.max_diameter 