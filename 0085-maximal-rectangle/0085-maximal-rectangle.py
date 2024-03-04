class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        left_smaller=[0]*(n)
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                left_smaller[i]=stack[-1]+1
            stack.append(i)
        
        stack=[]
        right_smaller=[n-1]*(n)
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right_smaller[i]=stack[-1]-1
            stack.append(i)
        max_area=float('-inf')
        for i in range(n):
            max_area=max(max_area,heights[i]*(right_smaller[i]-left_smaller[i]+1))
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        heights=[0]*(n)
        max_area=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            area=self.largestRectangleArea(heights)
            max_area=max(area,max_area)
        return max_area