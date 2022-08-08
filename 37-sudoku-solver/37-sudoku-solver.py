class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def helper_valid(board,r,c,n_str):
            for j in range(9):
                if board[r][j]==n_str:
                    return False
            for i in range(9):
                if board[i][c]==n_str:
                    return False
            x=r//3
            y=c//3
            for i in range(3*x,3*x+3):
                for j in range(3*y,3*y+3):
                    if board[i][j]==n_str:
                        return False
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    for n_str in "123456789":
                        if helper_valid(board,i,j,n_str):
                            board[i][j]=n_str
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
    