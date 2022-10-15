class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def check_cycle(node,graph,visited):
            if visited[node]==2:
                return True
            visited[node]=2
            for neighbour in graph[node]:
                if visited[neighbour]!=1:
                    if check_cycle(neighbour,graph,visited):
                        return True
            visited[node]=1
            return False
                
        n=len(graph)
        visited=[0]*(n)
        for i in range(n):
            if visited[i]==0:
                if check_cycle(i,graph,visited):
                    continue
        answer=[]
        for i in range(n):
            if visited[i]==1:
                answer.append(i)
        return answer