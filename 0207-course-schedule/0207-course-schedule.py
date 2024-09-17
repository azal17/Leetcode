
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}

        for dependent, independent in prerequisites:
            adj[independent].append(dependent)

        def dfs(node, visited, pathvis):
            visited.add(node)
            pathvis[node] = 1


            for neigh in adj[node]:
                if neigh not in visited:
                    if dfs(neigh, visited, pathvis):
                        return True
                elif pathvis[neigh] == 1:
                    return True

            pathvis[node] = 0
            return False

        visited = set()
        pathvis = [0] * numCourses
        for i in range(numCourses):
            if i not in visited:
                if dfs(i, visited, pathvis):
                    return False
        return True
