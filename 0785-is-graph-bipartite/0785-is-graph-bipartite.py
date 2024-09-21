class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, color):
            for n in graph[node]:
                if colors[n] == -1:
                    colors[n] = 1- colors[node]
                    if not dfs(n,colors):
                        return False
                elif colors[n] == colors[node]:
                    return False
            return True

        
        n = len(graph)
        colors = [-1]*n
        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                if not dfs(i,colors):
                    return False
        return True      