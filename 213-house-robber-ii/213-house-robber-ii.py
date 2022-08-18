class Solution:
    def rob1(self,nums):
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*(n)
        prev1=nums[0]
        prev2=0
        for i in range(1,n):
            take=nums[i]
            if i>1:
                take+=prev2
            not_take=0+prev1
            cur=max(take,not_take)
            prev2=prev1
            prev1=cur
        return prev1
    def rob(self, nums: List[int]) -> int:

        
        n1=len(nums)
        if n1==1:
            return nums[0]
        temp1,temp2=[],[]
        for i in range(n1):
            if i!=0:
                temp1.append(nums[i])
            if i!=n1-1:
                temp2.append(nums[i])
        a=self.rob1(temp1)
        b=self.rob1(temp2)
        return max(a,b)
         