class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2=sorted(nums)
        N=len(nums)
        l,r=0,N
        for i,n in enumerate(nums):
            if nums[i]!=nums2[i]:
                l=max(l,i)
                r=min(r,i)
        if r==N:
            return 0
        return l-r+1
                         
                
        