import math
class Solution:
    def SumByD(self,arr,div):
        n=len(arr)
        total_sum=0
        for i in range(n):
            total_sum+=math.ceil(arr[i]/div)
        return total_sum
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        if n>threshold:
            return -1
        low,high=1,max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.SumByD(nums,mid)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low