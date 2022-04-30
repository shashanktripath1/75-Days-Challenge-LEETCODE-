class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        '''
        1. use the equations and values to construct a graph of a/b and b/a values.
        2. iterate through the queries and call BFS/DFS to evaualate the each queries.
        3. if query evalautes return result if not return -1
        4. store the result in an array with decimal division.
        5. return the result
        '''
        
        G = collections.defaultdict(list)
        
        for i,[a,b] in enumerate(equations):
            G[a].append((b,values[i]))
            G[b].append((a,1/values[i]))
        
        def bfs(x,y):
            
            if not x in G: return -1.0
            
            Q = deque([(x,1)])
            visited = set()
            
            while(Q):
                a, value = Q.popleft()
                
                if a == y: return value
                if not a in G: return -1
                
                visited.add(a)
                
                for (b,currValue) in G[a]:
                    if b in visited: continue
                    Q.append((b,value*currValue))
            
            return -1
        
        result = []
        for [x,y] in queries:
            result.append(bfs(x,y))
        
        return result
