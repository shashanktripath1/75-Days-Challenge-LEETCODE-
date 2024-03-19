from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create the adjacency list to depict airports and flights in
        # the form of a graph.
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # Create a queue which stores the node and their distances from the
        # source in the form of (stops, (node, cost)) with 'stops' indicating 
        # the no. of nodes between src and current node.
        queue = deque([(0, src, 0)])
        
        # Distance array to store the updated distances from the source.
        dist = [float('inf')] * n
        dist[src] = 0

        # Iterate through the graph using a queue like in Dijkstra with 
        # popping out the element with min stops first.
        while queue:
            stops, node, cost = queue.popleft()

            # We stop the process as soon as the limit for the stops reaches.
            if stops > k:
                continue
            
            for adj_node, adj_w in adj[node]:
                # We only update the queue if the new calculated dist is
                # less than the prev and the stops are also within limits.
                if cost + adj_w < dist[adj_node] and stops <= k:
                    dist[adj_node] = cost + adj_w
                    queue.append((stops + 1, adj_node, cost + adj_w))

        # If the destination node is unreachable return '-1'
        # else return the calculated dist from src to dst.
        return dist[dst] if dist[dst] != float('inf') else -1

