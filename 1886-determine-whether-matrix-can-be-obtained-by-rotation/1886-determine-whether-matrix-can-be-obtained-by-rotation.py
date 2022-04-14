class Solution:
    def rotate(self,mat):
        N=len(mat)
        for i in range(N):
            for j in range(i+1,N):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for row in range(N):
            mat[row].reverse()
        return mat
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True
        for i in range(3):
            self.rotate(mat)
            if target==mat:
                return True
        return False
        