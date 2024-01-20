#Noore's voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        n=len(nums)
        element=None
        for i in range(n):
            if cnt==0:
                element=nums[i]
                cnt+=1
            elif nums[i]==element:
                cnt+=1
            else:
                cnt-=1
        return element