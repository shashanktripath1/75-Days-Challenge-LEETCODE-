class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
        self.counter = 0
    
    def wadd(self, w):
        curr = self
        curr.counter += 1
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.counter += 1
        curr.eow = True
    
    def wremove(self, w):
        curr= self
        curr.counter -= 1
        for c in w:
            if c in curr.children:
                curr = curr.children[c]
                curr.counter -= 1
    
class Solution:
    def findWords(self, b: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.wadd(w)
        
        rows, cols = len(b), len(b[0])
        ans, vs = set(), set()
        
        def dfs(r,c,n,w):
            if (r<0 or c<0 or 
                r==rows or c==cols or
               (r,c) in vs or b[r][c] not in n.children or
                n.children[b[r][c]].counter < 1):
                return
            
            vs.add((r,c))
            n = n.children[b[r][c]]
            w += b[r][c]
            if n.eow:
                n.eow = False
                ans.add(w)
                root.wremove(w)
                
            dfs(r+1,c,n,w)
            dfs(r-1,c,n,w)
            dfs(r,c+1,n,w)
            dfs(r,c-1,n,w)
            
            vs.remove((r,c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
                
        return list(ans)
            
