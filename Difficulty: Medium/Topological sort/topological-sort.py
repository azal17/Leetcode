from queue import Queue

class Solution:
  
    def topoSort(self, V, adj):
        queue = Queue()     
        result = []          
        indegree = [0] * V   
        
        for i in range(V):
            for neighbor in adj[i]:
                indegree[neighbor] += 1  
        
 
        for i in range(V):
            if indegree[i] == 0:
                queue.put(i)

        while not queue.empty():
            node = queue.get()
            result.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.put(neighbor)
        
        return result

            
            
        
        



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends