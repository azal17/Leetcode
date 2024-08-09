
class Solution:
    
    def dfsOfGraph(self, V, adj):
        dfs_traversal = []
        visited = set()
    
        def dfs(v):
            visited.add(v)
            dfs_traversal.append(v)
            for neighbor in adj[v]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        
        return dfs_traversal



#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends