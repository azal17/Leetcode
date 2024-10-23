# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = Queue()
        q.put(root)
        result = []
        flag = 0 

        while not q.empty():
            size = q.qsize()
            level = []
            
            for _ in range(size):
                node = q.get()
                level.append(node.val)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        
            if flag:
                level.reverse()
            
            result.append(level)
            flag ^= 1  
        
        return result
