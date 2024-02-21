class Solution:
    def rob1(self, nums: List[int]) -> int:
        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=prev2
            not_pick=0+prev
            cur=max(pick,not_pick)
            prev2=prev
            prev=cur
        return prev
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==1:
            return nums[0]
        temp1,temp2=[],[]
        for i in range(n):
            if i!=0:
                temp1.append(nums[i])
            if i!=n-1:
                temp2.append(nums[i])
        ans1=self.rob1(temp1)
        ans2=self.rob1(temp2)
        return max(ans1,ans2)