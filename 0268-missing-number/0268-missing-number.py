class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        hash1=[0]*(n+1)
        for i in range(n):
            hash1[nums[i]]+=1
        for i in range(n+1):
            if hash1[i]==0 :
                return i
        return -1
