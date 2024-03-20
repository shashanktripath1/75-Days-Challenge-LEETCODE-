class Solution:
    def findTheCity(self, n, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Fill distance matrix with edge weights
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Set diagonal elements to 0
        for i in range(n):
            dist[i][i] = 0
        
        # Floyd-Warshall algorithm to find shortest distances between all pairs of vertices
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Initialize variables to track the city with the minimum reachable cities
        cnt_city = n
        city_no = -1

        for city in range(n):
            cnt = 0
            for adj_city in range(n):
                if dist[city][adj_city] <= distanceThreshold:
                    cnt += 1

            if cnt <= cnt_city:
                cnt_city = cnt
                city_no = city

        return city_no


