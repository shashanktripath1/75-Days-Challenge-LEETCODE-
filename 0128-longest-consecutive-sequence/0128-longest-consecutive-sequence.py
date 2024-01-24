class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        cnt_crt=0
        last_smaller=float('-inf')
        longest=1
        nums.sort()

        for i in range(n):
            if nums[i]-1==last_smaller:
                cnt_crt+=1
                last_smaller=nums[i]
            elif nums[i]!=last_smaller:
                cnt_crt=1
                last_smaller=nums[i]
            longest=max(longest,cnt_crt)
            
        return longest
            