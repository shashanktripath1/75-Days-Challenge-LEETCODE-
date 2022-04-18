class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        list=[]
        for i in range(len(l)):
            s=nums[l[i]:r[i]+1]
            s.sort()
            d=Solution().helper(s)
            list.append(d)
        return list
    def helper(self,arr):
        if len(arr)==2:
            return True
        for i in range(1,len(arr)-1):
            if arr[i]-arr[i-1]!=arr[i+1]-arr[i]:
                return False
        return True
        