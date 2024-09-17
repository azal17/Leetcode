from queue import Queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i: [] for i in range(numCourses)}

        for dependent, independent in prerequisites:
            adj[independent].append(dependent)

        vis = set()  
        q = Queue() 
        indegree = [0] * numCourses 
        result = [] 
        count = 0
        for i in range(numCourses):
            for n in adj[i]:
                indegree[n] += 1 

        for n in range(numCourses):
            if indegree[n] == 0:
                q.put(n)

        while not q.empty():
            nodee = q.get()
            result.append(nodee)
            count +=1
            for j in adj[nodee]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.put(j)
        return count == numCourses
