#User function Template for python3
from typing import List
class DisjointSet:
    def __init__(self, n: int):
        self.rank = [0] * (n + 1)  
        self.parent = [i for i in range(n + 1)]  
        self.size = [1]*(n+1)


    def find(self, node: int) -> int:
        if node != self.parent[node]:  
            self.parent[node] = self.find(self.parent[node])  
        return self.parent[node]

    def unionByRank(self, u: int, v: int):
        ultParentU = self.find(u)
        ultParentV = self.find(v)

        if ultParentU == ultParentV:
            return 
        if self.rank[ultParentU] < self.rank[ultParentV]:
            self.parent[ultParentU] = ultParentV
        elif self.rank[ultParentU] > self.rank[ultParentV]:
            self.parent[ultParentV] = ultParentU
        else:
            self.parent[ultParentV] = ultParentU
            self.rank[ultParentU] += 1  
    def unionBySize(self,u: int,v: int):
        ultParentU = self.find(u)
        ultParentV = self.find(v)

        if ultParentU == ultParentV:
            return  
        if self.size[ultParentU] < self.size[ultParentV]:
            self.parent[ultParentU] = ultParentV
            self.size[ultParentV] +=  self.size[ultParentU] 
        else:
           self.parent[ultParentV] = ultParentU
           self.size[ultParentU] +=  self.size[ultParentV] 


class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        
        #code here
        edges = []
        for node in range(V):
            for neigh, weight in adj[node]:
                edges.append((weight, node, neigh))
        ds = DisjointSet(V)
        edges.sort()
        summ = 0
        
        for wt, node, neigh in edges:
            if ds.find(node) != ds.find(neigh):
                summ += wt
                ds.unionBySize(node, neigh)
                
        return summ
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))

# } Driver Code Ends