# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# T.C = O(N^2), S.C = O(N)
class Solution:
    def __init__(self):
        self.maxi = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        if root is None:
            return None
        lh, rh = self.find(root.left), self.find(root.right)
        
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        self.maxi = max(self.maxi, lh + rh)
        return self.maxi

    def find(self, node):
        if node is None:
            return 0
        lh, rh = self.find(node.left), self.find(node.right)
        return max(lh, rh) +1



