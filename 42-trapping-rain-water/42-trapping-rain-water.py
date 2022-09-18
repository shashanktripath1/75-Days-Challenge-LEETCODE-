class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        l_max,r_max=0,0
        ans=0
        while left<right:
            if height[left]<height[right]:
                l_max=max(l_max,height[left])
                ans+=l_max-height[left]
                left+=1
            else:
                r_max=max(r_max,height[right])
                ans+=r_max-height[right]
                right-=1
        return ans
