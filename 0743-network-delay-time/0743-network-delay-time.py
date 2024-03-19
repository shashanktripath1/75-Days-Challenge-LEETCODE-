import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list to represent the graph
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Create a min-heap (priority queue) to store (time, node) pairs
        pq = [(0, k)]
        # Dictionary to store the shortest time to reach each node
        dist = {}
        
        # Dijkstra's algorithm
        while pq:
            time, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = time
            for neighbor, neighbor_time in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (time + neighbor_time, neighbor))
        
        # Check if all nodes are reachable
        if len(dist) != n:
            return -1
        
        # Return the maximum time taken to reach a node
        return max(dist.values())
