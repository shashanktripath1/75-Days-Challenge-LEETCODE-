class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        dx = defaultdict(set)
        dy = defaultdict(set)
        
        for x,y in stones:
            dx[x].add((x, y))
            dy[y].add((x, y))
            
        visited = set()
        
        def dfs(x, y):
            visited.add((x, y))
            child = (dx[x].union(dy[y]) - visited)
            for p, q in child:
                dfs(p, q)
        
        cc = 0
        for x,y in stones:
            if(not (x,y) in visited):
                dfs(x, y)
                cc+=1
        
        return len(stones)-cc
        