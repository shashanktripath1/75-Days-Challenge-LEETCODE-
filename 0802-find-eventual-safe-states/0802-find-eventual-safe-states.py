class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        indegree=[0]*(n)
        adj=[[]for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                adj[v].append(u)
                indegree[u]+=1
        queue=deque()
        for v in range(n):
            if indegree[v]==0:
                queue.append(v)
        ans=[]
        while queue:
            u=queue.popleft()
            ans.append(u)
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        return sorted(ans)
        
            