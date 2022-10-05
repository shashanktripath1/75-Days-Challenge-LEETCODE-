class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r,c,src_color):
            if r<0 or r>=m or c<0 or c>=n or image[r][c]==color  or image[r][c]!=src_color:
                return 0
            image[r][c]=color
            dfs(r+1,c,src_color)
            dfs(r-1,c,src_color)
            dfs(r,c-1,src_color)
            dfs(r,c+1,src_color)
            

        m,n=len(image),len(image[0])
        dfs(sr,sc,src_color=image[sr][sc])
        return image