class Solution:
    def equationsPossible(self, equations) -> bool:
        parent = {}
        rank = {}
        
        for eq in equations:
            x, y = eq[0], eq[-1]
            parent[x], parent[y], rank[x], rank[y] = x, y, 0, 0
                    
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(x, y):
            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[y] > rank[x]:
                parent[x] = y
            else:
                parent[y] = x
                rank[x] += 1
        
        nonEquals = []
        
        for eq in equations:
            e = eq[1]
            
            if e == '=':
                x, y = eq[0], eq[-1]
                px, py = find(x), find(y)
                
                if px != py:
                    union(px, py)
            else:
                nonEquals.append(eq)
            
        for eq in nonEquals:
            x, y= eq[0], eq[-1]
            px, py = find(x), find(y)
                
            if px == py:
                return False
        
        return True
