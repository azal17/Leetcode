class Solution:
    def maxNumOfSubstrings(self, S: str) -> List[str]:
        mins = [float('inf')] * 26
        maxs = [-1] * 26
        exists = [False] * 26
        prefix_sum = [[0] * 26 for _ in range(len(S) + 1)]
        
        for i, char in enumerate(S):
            idx = ord(char) - ord('a')
            for j in range(26):
                prefix_sum[i + 1][j] = prefix_sum[i][j]
            prefix_sum[i + 1][idx] += 1
            mins[idx] = min(mins[idx], i)
            maxs[idx] = max(maxs[idx], i)
            exists[idx] = True

        graph = [[False] * 26 for _ in range(26)]
        for i in range(26):
            if exists[i]:
                for j in range(26):
                    if prefix_sum[maxs[i] + 1][j] - prefix_sum[mins[i]][j] > 0:
                        graph[i][j] = True

        stack = []
        visited = [False] * 26
        for i in range(26):
            if exists[i] and not visited[i]:
                self.dfs1(i, graph, stack, visited)
        
        batch = 0
        batches = [-1] * 26
        degree = [0] * 26
        
        while stack:
            v = stack.pop()
            if batches[v] < 0:
                self.dfs2(v, graph, batches, batch, degree)
                batch += 1
        res = []
        for i in range(batch - 1, -1, -1):
            if degree[i] == 0:
                min_idx = float('inf')
                max_idx = -1
                for j in range(26):
                    if batches[j] == i:
                        min_idx = min(mins[j], min_idx)
                        max_idx = max(maxs[j], max_idx)
                res.append(S[min_idx:max_idx + 1])
        
        return res
    
    def dfs1(self, v, graph, stack, visited):
        if not visited[v]:
            visited[v] = True
            for i in range(26):
                if graph[v][i] and not visited[i]:
                    self.dfs1(i, graph, stack, visited)
            stack.append(v)
    
    def dfs2(self, v, graph, batches, batch, degree):
        if batches[v] < 0:
            batches[v] = batch
            for i in range(26):
                if graph[i][v]:
                    self.dfs2(i, graph, batches, batch, degree)
        else:
            if batches[v] != batch:
                degree[batches[v]] += 1
