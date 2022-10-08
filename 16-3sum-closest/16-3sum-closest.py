class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 10**5
        nums.sort()
        for i in range(n-2):
            t = target - nums[i]
            left = bisect.bisect_left(nums[i+1:], t//2) + i+1
            if left >= n-1:
                left = n-2
            right = left + 1
            while left > i and right < n:
                eq = nums[left] + nums[right] - t
                if eq == 0:
                    return target
                elif eq > 0:
                    left -= 1
                else:
                    right += 1
                if abs(eq) < abs(ans):
                    ans = eq
        return target + ans