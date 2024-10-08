from typing import List

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        
        distance_array = [float('inf')] * V
        distance_array[S] = 0  
        s = set()
        s.add((0,S))

        while s:
            wt, node = min(s) 
            s.remove((wt, node))  
            for neighbor, weight in adj[node]:
                new_distance = wt + weight
                if new_distance < distance_array[neighbor]:
                    distance_array[neighbor] = new_distance
                    s.add((new_distance, neighbor))  
        return distance_array



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends