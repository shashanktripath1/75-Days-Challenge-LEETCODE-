class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_0,count_1,count_2=0,0,0
        for i in nums:
            if i==0:
                count_0+=1
            elif i==1:
                count_1+=1
            else:
                count_2+=1
        for i in range(count_0):
            nums[i]=0
        for i in range(count_0,count_0+count_1):
            nums[i]=1
        for i in range(count_0+count_1,len(nums)):
            nums[i]=2
        return nums
        