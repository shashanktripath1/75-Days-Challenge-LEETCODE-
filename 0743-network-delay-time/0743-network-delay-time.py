import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        pq=[(0,k)]
        dist={}
        while pq:
            time,node=heapq.heappop(pq)
            if node in dist:
                continue
            dist[node]=time
            for neighbour,neighbour_time in graph[node]:
                if neighbour not in dist:
                    heapq.heappush(pq,(time+neighbour_time,neighbour))
        if len(dist)!=n:
            return -1
        return max(dist.values())
    
