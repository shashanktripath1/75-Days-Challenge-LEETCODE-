class Solution:
    def upperBound(self,arr, n, x):
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
        # maybe an answer
            if arr[mid] > x:
                ans = mid
            # look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1  # look on the right
        return ans

    def lowerBound(self,arr, n, x):
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
        # maybe an answer
            if arr[mid] >= x:
                ans = mid
            # look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1  # look on the right
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        lb=self.lowerBound(nums,n,target)
        if lb==n or nums[lb]!=target:
            return [-1,-1]
        ub=self.upperBound(nums,n,target)
        return [lb,ub-1]