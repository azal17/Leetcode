from queue import Queue

def cycleDetection(edges, n, m):
    def bfs(start_node):
        q = Queue()
        q.put(start_node)
        visited = set()
        parent = {start_node: None}
        visited.add(start_node)

        while not q.empty():
            node = q.get()

            for sublist in edges:
                if node in sublist:
                    for neighbor in sublist:
                        if neighbor != node:
                            if neighbor in visited:
                                
                                if parent[node] != neighbor:
                                    return True
                            else:
                                visited.add(neighbor)
                                q.put(neighbor)
                                parent[neighbor] = node

        return False

    visited_nodes = set()
    for node in range(1, n + 1):
        if node not in visited_nodes:
            if bfs(node):
                return 'Yes'
            visited_nodes.update(visited_nodes)  

    return 'No'