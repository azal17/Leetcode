# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.postorder(root,array)
        return array
    def postorder(self,node: Optional[TreeNode], a: List[int]) -> None:
        if node is None:
            return
        self.postorder(node.left,a)
        self.postorder(node.right,a)
        a.append(node.val)
        