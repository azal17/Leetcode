#User function Template for python3
from typing import List
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        parent = [-1] * (n + 1)
        dist = [float('inf')] * (n + 1)
        min_heap = []
        dist[1] = 0
        parent[1] = 1
        heapq.heappush(min_heap, (0, 1))
        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        while min_heap:
            curr_dist, node1 = heapq.heappop(min_heap)
            if curr_dist <= dist[node1]:
                for neighbor, weight in graph[node1]:
                    new_dist = curr_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        parent[neighbor] = node1
                        heapq.heappush(min_heap, (new_dist, neighbor))

        if dist[n] == float('inf'):
            return [-1]

        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        path.reverse()
        return  [dist[n]] + path


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends