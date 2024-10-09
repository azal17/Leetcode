#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency list representation
    '''
    V: number of vertices in the graph
    edges: list of edges (u, v, wt) where u -> v with weight wt
    S: source vertex
    '''
    def bellman_ford(self, V, edges, S):
        dist = [10**8] * V
        dist[S] = 0

        for i in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != 10**8 and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        for u, v, wt in edges:
            if dist[u] != 10**8  and dist[u] + wt < dist[v]:
                return {-1}

        return dist

                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends