#T.C = ElogV or (V+E)logV, set will give T.C = O(V2 + E)
from typing import List

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        
        distance_array = [float('inf')] * V
        distance_array[S] = 0  
        s = {(0, S)}  

        while s:
            wt, node = min(s) 
            s.remove((wt, node))  
            for neighbor, weight in adj[node]:
                new_distance = wt + weight
                if new_distance < distance_array[neighbor]:
                    distance_array[neighbor] = new_distance
                    s.add((new_distance, neighbor))  
        return distance_array
