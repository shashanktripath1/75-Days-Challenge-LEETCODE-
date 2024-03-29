class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!='O':
                return
            board[i][j]='#'  #CONVERTING TO A DOLLAR SIGN
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        m,n=len(board),len(board[0])
        if m==0:
            return None
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1:
                    dfs(i,j)#CALLING DFS ON ALL BORDER 0'S
                if j==0 or j==n-1:
                    dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'#LEFT OUT ZEROES ARE TURNED TO X
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='#':
                    board[i][j]='O'#CONVERTING BORDER ZEROES INTO ORIGINAL FORMS FROM # TO 'o'
        return board
        