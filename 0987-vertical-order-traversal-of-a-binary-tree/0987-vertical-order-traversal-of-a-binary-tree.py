# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(lambda: defaultdict(list))
        q = deque([(root, 0, 0)]) 

        while q:
            node, x, y = q.popleft()
            nodes[x][y].append(node.val)

            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))

        result = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y])) 
            result.append(col)

        return result