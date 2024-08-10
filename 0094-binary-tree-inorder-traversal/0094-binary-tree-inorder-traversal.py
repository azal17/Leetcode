# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.inorder(root, array)
        return array
    
    def inorder(self, root: Optional[TreeNode], a: List[int]) -> None:
        if root is None:
            return
        self.inorder(root.left, a)  
        a.append(root.val)          
        print(root.val)         
        self.inorder(root.right, a) 
