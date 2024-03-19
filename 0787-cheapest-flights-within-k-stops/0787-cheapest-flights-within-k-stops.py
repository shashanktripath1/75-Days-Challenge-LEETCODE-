from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[]for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))
        queue=deque()
        queue.append((0,src,0))#(stops,node,cost)
        dist=[float('inf')]*(n)
        dist[src]=0
        while queue:
            stops,node,cost=queue.popleft()
            if stops>k:
                continue
            for adj_node,cost_adj in adj[node]:
                if cost+cost_adj<dist[adj_node] and stops<=k:
                    dist[adj_node]=cost+cost_adj
                    queue.append((stops+1,adj_node,cost+cost_adj))
        return dist[dst] if dist[dst]!=float('inf') else -1
    