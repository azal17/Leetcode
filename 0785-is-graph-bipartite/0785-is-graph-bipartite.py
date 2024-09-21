from queue import Queue
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        color = [-1]*n

        for i in range(n):
            if color[i] == -1:
                    
                q = Queue()
                q.put(i)
                color[i] = 0

                while not q.empty():
                    node = q.get()

                    for n in graph[node]:
                        if color[n] == -1:
                            color[n] = 1 - color[node]
                            q.put(n)
                        elif color[n] == color[node]:
                            return False
        return True
            