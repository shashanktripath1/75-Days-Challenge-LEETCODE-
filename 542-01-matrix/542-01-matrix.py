class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited=set()
        queue=deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    visited.add((i,j))
                    queue.append((i,j))
        while queue:
            a,b=queue.popleft()
            for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_a,new_b=a+direction[0],b+direction[1]
                if new_a>=0 and new_a<=len(mat)-1 and new_b>=0 and new_b<=len(mat[0])-1 and (new_a,new_b) not in visited:
                    mat[new_a][new_b]=mat[a][b]+1
                    visited.add((new_a,new_b))
                    queue.append((new_a,new_b))
        return mat
