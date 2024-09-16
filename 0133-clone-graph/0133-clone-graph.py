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
        queue = Queue() 
        queue.put(node)  
        mpp[node] = Node(node.val) 
        while not queue.empty():
            n = queue.get()  

            for neigh in n.neighbors: 
                if neigh not in mpp:
                    mpp[neigh] = Node(neigh.val)  
                    queue.put(neigh)  
                mpp[n].neighbors.append(mpp[neigh])  
        
        return mpp[node]