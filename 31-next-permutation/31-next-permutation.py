class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N=len(nums)
        pivot=0
        for i in range(N-1,0,-1):
            if nums[i-1]<nums[i]:
                pivot=i
                break
        if pivot==0:
            nums.sort()
            return
        #find the number just greater than pivot
        swap=N-1
        while nums[pivot-1]>=nums[swap]:
            swap-=1
        #swap
        nums[swap],nums[pivot-1]=nums[pivot-1],nums[swap]
        nums[pivot:]=sorted(nums[pivot:])
                
        