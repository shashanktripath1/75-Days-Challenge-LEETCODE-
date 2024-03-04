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