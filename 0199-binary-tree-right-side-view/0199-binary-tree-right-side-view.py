# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        def reverseinorder(root,level):
            if root is None:
                return
            if level == len(array):
                array.append(root.val)
            reverseinorder(root.right, level+1)
            reverseinorder(root.left, level+1)
        reverseinorder(root, 0)
        return array