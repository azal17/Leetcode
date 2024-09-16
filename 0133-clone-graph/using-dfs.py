"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from queue import Queue
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        mpp = {}
        def dfs(node):
            if node in mpp:
                return mpp[node]
            
            mpp[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                mpp[node].neighbors.append(dfs(neighbor))
            
            return mpp[node]
        return dfs(node)
