class Solution:
    def helper(self,row,col,pos_dig,neg_dig,ans,board,n):
        if row==n:
            store_ans=["".join(r) for r in board]
            ans.append(store_ans)
        for c in range(n):
            if c in col or row+c in pos_dig or row-c in neg_dig:
                continue
            col.add(c)
            pos_dig.add(row+c)
            neg_dig.add(row-c)
            board[row][c]='Q'
            
            self.helper(row+1,col,pos_dig,neg_dig,ans,board,n)
            
            col.remove(c)
            pos_dig.remove(row+c)
            neg_dig.remove(row-c)
            board[row][c]="."
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pos_dig=set()
        neg_dig=set()
        ans=[]
        board=[["."]*n for _ in range(n )]
        self.helper(0,col,pos_dig,neg_dig,ans,board,n)
        return ans