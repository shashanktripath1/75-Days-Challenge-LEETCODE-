class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M=len(board)
        N=len(board[0])
        P=len(word)
        def helper(r,c,pos):
            if pos>=P:
                return True
            elif 0<=r<M and 0<=c<N and board[r][c]==word[pos]:
                temp=board[r][c]
                board[r][c]=None
                if helper(r+1,c,pos+1) or helper(r-1,c,pos+1) or helper(r,c+1,pos+1) or helper(r,c-1,pos+1):
                    return True
                board[r][c]=temp
            return False
        
        
        
        for r in range(M):
            for c in range(N):
                if helper(r,c,0):
                    return True
        return False
                