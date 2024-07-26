
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize the adjacency matrix
        inf = float('inf')
        dist = [[inf] * n for _ in range(n)]
        
        # Distance to self is always 0
        for i in range(n):
            dist[i][i] = 0
        
        # Populate the adjacency matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 2: Apply Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 3: Count the number of reachable cities for each city
        reachable_cities_count = []
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            reachable_cities_count.append(count)
        
        # Step 4: Find the city with the smallest number of reachable cities
        # If there are multiple, return the city with the greatest index
        min_reachable = min(reachable_cities_count)
        city = -1
        for i in range(n):
            if reachable_cities_count[i] == min_reachable:
                city = i
        
        return city
