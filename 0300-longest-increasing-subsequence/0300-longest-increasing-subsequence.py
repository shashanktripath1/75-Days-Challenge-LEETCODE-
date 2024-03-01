class Solution:
    #space optimized using next and cur array
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        next=[0]*(n+1)
        cur=[0]*(n+1)
        for ind in range(n-1,-1,-1):
            for prev_ind in range(ind-1,-2,-1):
                not_take=0+next[prev_ind+1]#due to coordinate shift
                take=0
                if prev_ind==-1 or nums[ind]>nums[prev_ind]:
                    take=1+next[ind+1]
                cur[prev_ind+1]=max(not_take,take)
            next=cur
        return cur[-1+1]
    