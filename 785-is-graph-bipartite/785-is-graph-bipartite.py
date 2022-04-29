class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        u = [i for i in range(n)]
        
        def find(i):
            if i == u[i]: return i
            else: 
                u[i] = find(u[i])
                return u[i]
            
        def union(a, b):
            r_a = find(a)
            r_b = find(b)
            if r_a != r_b: 
                u[r_a] = r_b
                u[a] = r_b
                
        for g in range(len(graph)):
            root = find(g)
            for i in range(1, len(graph[g])):
                union(graph[g][i], graph[g][i-1])
                if root == find(graph[g][i]) or root == find(graph[g][i - 1]):
                    return False
        return True
            