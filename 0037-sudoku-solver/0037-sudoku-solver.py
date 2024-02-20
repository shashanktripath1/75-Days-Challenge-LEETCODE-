class Solution:
    def is_possible(self,row,col,c,board):
        for i in range(9):
            if board[i][col]==c:
                return False
            if board[row][i]==c:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==c:
                return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    for c in "123456789":
                        if self.is_possible(i,j,c,board)==True:
                            board[i][j]=c
                            if self.solveSudoku(board)==True:
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
        