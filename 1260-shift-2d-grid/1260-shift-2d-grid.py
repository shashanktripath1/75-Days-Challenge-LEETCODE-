class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M,N=len(grid),len(grid[0])
        def twod_oned(r,c):
            return r*N+c
        def oned_twod(v):
            return [v//N,v%N]
        res=[[0]*N for j in range(M)]
        for i in range(M):
            for j in range(N):
                newVal=(twod_oned(i,j)+k)%(M*N)
                newR,newC=oned_twod(newVal)
                res[newR][newC]=grid[i][j]
        return res
        