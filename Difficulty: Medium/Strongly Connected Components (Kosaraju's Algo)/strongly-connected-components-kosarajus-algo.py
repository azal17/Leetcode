#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        def dfs1(node, vis, adj, stack):
            vis.add(node)
            for neighbour in adj[node]:
                if neighbour not in vis:
                    dfs1(neighbour, vis, adj, stack)
            stack.append(node)
        
        def dfs2(node, vis, transposedadj):
            vis.add(node)
            for neighbour in transposedadj[node]:
                if neighbour not in vis:
                    dfs2(neighbour, vis, transposedadj)
        def transposedgraph(V, adj):
            transposedadj = [[] for _ in range(V)]
            for i in range(V):
                for neighbour in adj[i]:
                    transposedadj[neighbour].append(i)
            return transposedadj
        vis = set()
        stack = []
        
        for i in range(V):
            if i not in vis:
                dfs1(i, vis, adj, stack)
        
        transposedadj =  transposedgraph(V, adj)
        
        vis = set()
        count = 0
        
        while stack:
            node = stack.pop()
            if node not in vis:
                dfs2(node, vis, transposedadj)
                count += 1
        
        return count
#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends