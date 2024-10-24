# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        array = []

        while cur:
            if cur.left is None:
                array.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if prev.right is None:
                    prev.right = cur
                    array.append(cur.val)
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return array