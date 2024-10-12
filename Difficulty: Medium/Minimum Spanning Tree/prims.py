#T.C = eloge, S.C = E
#PRIM'S ALGORITHM
import heapq
from typing import List
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        vis = [False]*V
        mst = []
        min_heap = []
        
        heapq.heappush(min_heap, (0 ,0 ,-1 ))
        sum = 0
        while min_heap:
            wt, node, parent =  heapq.heappop(min_heap)
            if vis[node]:
                continue
            vis[node] = True
            if parent != -1:
                sum += wt
                
            for neigh, edge_wt in adj[node]:
                 heapq.heappush(min_heap, (edge_wt ,neigh , node ))
        return sum
                 


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
