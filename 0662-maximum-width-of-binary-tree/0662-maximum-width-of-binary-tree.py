# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        q = deque([(root, 0)])
        width = 0
        while q:
            size = len(q)
            _, minn = q[0]
            for i in range(size):
                node, curr = q.popleft()
                curr -= minn
                if i == 0:
                    first = curr
                if i == size - 1:
                    last = curr
                if node.left:
                    q.append((node.left, 2*curr+1))
                if node.right:
                    q.append((node.right, 2*curr+2))
            width = max(width, last - first +1)
        return width

                