from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        smaller = [-1] * n
        tempNums = SortedList()
        for key, num in enumerate(nums[::-1]):
            smaller[n - key - 1] = tempNums.bisect_left(num)
            tempNums.add(num)
        return smaller