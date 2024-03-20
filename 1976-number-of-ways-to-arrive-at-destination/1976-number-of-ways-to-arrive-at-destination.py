import heapq

class Solution:
    def countPaths(self, n: int, paths: List[List[int]]) -> int:
        # Create an adjacency list for the given graph.
        adj = [[] for _ in range(n)]
        for path in paths:
            adj[path[0]].append((path[1], path[2]))
            adj[path[1]].append((path[0], path[2]))

        # Initialize distance array and ways array along with their first indices.
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        # Define modulo value.
        mod = 10**9 + 7

        # Define a priority queue (min heap).
        pq = [(0, 0)]

        # Iterate through the graph with the help of priority queue.
        while pq:
            dis, node = heapq.heappop(pq)

            for adjNode, edW in adj[node]:
                # If this is the first time reaching this node with a shorter distance,
                # update distance, push into priority queue, and keep the number of ways the same.
                if dis + edW < dist[adjNode]:
                    dist[adjNode] = dis + edW
                    heapq.heappush(pq, (dis + edW, adjNode))
                    ways[adjNode] = ways[node]

                # If encountering a node with the same short distance as before,
                # increment the number of ways.
                elif dis + edW == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod

        # Return the number of ways to reach the (n-1)th node modulo 10^9+7.
        return ways[n - 1] % mod

