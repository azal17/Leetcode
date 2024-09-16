def cycleDetection(edges, n, m):
    def dfs(node,parent,edges):
        vis.add(node)
        for subset in edges:
            if node in subset:
                for n in subset:
                    if n != node:
                        if n not in vis:
                            if dfs(n, node, edges):
                                return True
                        elif n != parent:
                            return True
        return False


    vis = set()
    for i in range(1, n+1):
        if i not in vis:
            if dfs(i, -1, edges):
                return "Yes"
    return "No"


   
