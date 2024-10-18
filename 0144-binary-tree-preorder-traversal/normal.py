# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# T.C = O(n), S.C = O(logn / h) , wc = O(n)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.preorder(root,array)
        return array

    def preorder(self, node: Optional[TreeNode], a: List[int]) -> None:
        if node is None:
            return
        a.append(node.val)
        self.preorder(node.left,a)
        self.preorder(node.right,a)
        
