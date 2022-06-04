class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posdig=set()#(r+c)
        negdig=set()#(r-c)
        res=[]
        board=[["."]*n for i in range(n)]
    #backtracking function
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posdig or (r-c) in negdig:
                    continue
                
                col.add(c)
                posdig.add(r+c)
                negdig.add(r-c)
                board[r][c]="Q"
                
                backtrack(r+1)
                
                col.remove(c)
                posdig.remove(r+c)
                negdig.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
                
    
        