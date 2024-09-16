#User function Template for python3

class Solution:
    
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
       
        stack = [0]
        visited = set()
        result = []
        
        while stack:
            node = stack.pop()
            
           
            if node not in visited:
                result.append(node)  
                visited.add(node)
                
                for neighbor in reversed(adj[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result


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