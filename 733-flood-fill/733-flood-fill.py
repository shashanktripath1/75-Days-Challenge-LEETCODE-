class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        visited=[]
        new_color=image[sr][sc]
        def dfs(sr,sc):
            if sr<0 or sr>=rows:
                return 0
            if sc<0 or sc>=cols:
                return 0
            if (sr,sc) in visited:
                return 0
            if image[sr][sc]!=new_color:
                return 0
            image[sr][sc]=color
            visited.append((sr,sc))
            dfs(sr+1,sc)
            dfs(sr-1,sc)
            dfs(sr,sc-1)
            dfs(sr,sc+1)
        dfs(sr,sc)
        return image
    
            
            