# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, root, target, path):
        if root is None:
            return False
        path.append(root)
        if root == target:
            return True
        if (root.left and self.findPath(root.left, target, path)) or \
        (root.right and self.findPath(root.right, target, path)):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1, path2 = [], []

        if not self.findPath(root, p, path1) or not self.findPath(root, q, path2):
            return None
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1
        i -= 1
        return path1[i] if i >= 0 else None
