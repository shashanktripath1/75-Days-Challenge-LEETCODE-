class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def helper(board,r,c,s):
            for j in range(9):
                if board[r][j]==s:
                    return False
            for i in range(9):
                if board[i][c]==s:
                    return False
            x,y=r//3,c//3
            for i in range(3*x,3*x+3):
                for j in range(3*y,3*y+3):
                    if board[i][j]==s:
                        return False
            return True
                    
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    for s in "123456789":
                        if helper(board,i,j,s):
                            board[i][j]=s
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]='.'
                    return False
        return True