#dfs approach
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i,c):
            if color[i]!=-1:
                if color[i]!=c:
                    return False
                return True
            color[i]=c
            for v in graph[i]:
                if not dfs(v,1-c):
                    return False
            return True
            
        n=len(graph)
        color=[-1]*(n)
        for i in range(n):
            if color[i]==-1:
                if not dfs(i,1):
                    return False
        return True
    
