class Solution:
    def dfs(self,row,col,ans,image,color,delRow,delCol,initial_color):
        ans[row][col]=color
        m=len(image)
        n=len(image[0])
        for i in range(4):
            nrow=row+delRow[i]
            ncol=col+delCol[i]
            if 0<=nrow<m and 0<=ncol<n and image[nrow][ncol]==initial_color and ans[nrow][ncol]!=color:
                self.dfs(nrow,ncol,ans,image,color,delRow,delCol,initial_color)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color=image[sr][sc]
        ans=[row[:] for row in image]
        delRow=[1,-1,0,0]
        delCol=[0,0,1,-1]
        self.dfs(sr,sc,ans,image,color,delRow,delCol,initial_color)
        return ans