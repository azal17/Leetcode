#User function Template for python3

from typing import List
from collections import deque

class Solution:
   
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
  
        bfs_traversal = []
        visited = [False] * V
        queue = deque()


        queue.append(0)
        visited[0] = True

        while queue:
            node = queue.popleft()
            bfs_traversal.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        
        return bfs_traversal

                
            


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends