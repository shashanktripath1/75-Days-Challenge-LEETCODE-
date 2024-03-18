class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        adjRev=[[] for _ in range(n)]
        indegree=[0]*(n)
        for i in range(n):
            for neighbour in graph[i]:
                adjRev[neighbour].append(i)
                indegree[i]+=1
        queue=deque()
        safeNodes=[]
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            node=queue.popleft()
            safeNodes.append(node)
            for neighbour in adjRev[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        return sorted(safeNodes)
        